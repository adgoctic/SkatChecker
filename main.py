# copyright: Emil Obert, 2022
import sys

import pandas as pd
from compare_values import *

playedCards = []
player_order = []

# cards played by each player in order played
hand_1 = []
hand_2 = []
hand_3 = []

'''
reads text file with card order in the format:
    CSV, 2 characters per card;
        first:
            suit, represented by letter:
                D: diamond
                H: heart
                S: spade
                C: club
        second:
            value, either number or letter:
                7-9: themselves
                0  : 10
                J  : Jack
                Q  : Queen
                K  : King
                A  : Ace
    LAST 2 CARDS ARE SET ASIDE ("SKAT") AND NOT PART OF THE PLAYED CARDS
    
    :returns: list of played cards as objects
'''
def read_file(fileName):
    playedCards_rf = []
    raw = pd.read_csv(fileName)
    ############################################################################
    #print("read_file found " + str(len(raw)) + " cards in the file")  #DEBUG####
    ############################################################################
    for element in raw:
        c = Card(element[0], element[1])
        playedCards_rf.append(c)
        ###############################################################
        #print("added " + element + " to playedCards_rf")  ###DEBUG########
        ###############################################################

    return playedCards_rf


'''
returns: boolean, true iff valid cardset provided
'''
def check_cardset(filename):
    #complete_set = set(read_file("complete.csv"))

    #####################################################################
    #for c in playedCards:
    #    print(c.to_string(), ' ')              #########DEBUG#################
    #    print(str(c))   # updated, overrode actual str() fct.
    #print(len(playedCards))
    #####################################################################

    #for card in playedCards:
    #    if len(complete_set) > 0 and complete_set.__contains__(card):   ##for some reason, contains not redundand (??????!!)
    #        complete_set.remove(card)
    #    else:
    #        return False
    #if len(complete_set) == 0:
    #    return True
    #else:
    #    return False

    complete_set = set(read_file("complete.csv"))
    my_set = set(read_file(filename))
    #return complete_set.difference(my_set) == {}
    return complete_set == my_set


'''
puts order the players must have been playing in in array player_order
    (e.g. [1,2,3,2,3,1,...])
'''
def order_grand():
    player_order = [1, 2, 3]

    for i in range(30):
        if i % 3 == 0:
            a = playedCards[i]
            b = playedCards[i + 1]
            c = playedCards[i + 2]

            if (compare_nonzero(b) > compare_nonzero(a)) and (a.suit == b.suit or b.value == 'J'):
                if (compare_nonzero(c) > compare_nonzero(b)) and (a.suit == c.suit or c.value == 'J'):
                    # player who was last goes first in next round      # ToDo: outsource these 3 variants to function
                    player_order.append(player_order[i + 2])
                    player_order.append(player_order[i])
                    player_order.append(player_order[i + 1])
                else:
                    # player who was second goes first in next round
                    player_order.append(player_order[i + 1])
                    player_order.append(player_order[i + 2])
                    player_order.append(player_order[i])
            else:
                # player order stays the same
                player_order.append(player_order[i])
                player_order.append(player_order[i + 1])
                player_order.append(player_order[i + 2])
    return player_order


def order_zero():
    player_order = [1, 2, 3]

    for i in range(30):
        if i % 3 == 0:
            a = playedCards[i]
            b = playedCards[i + 1]
            c = playedCards[i + 2]

            if (compare_zero(b) > compare_zero(a)) and (a.suit == b.suit):
                if (compare_zero(c) > compare_zero(b)) and (a.suit == c.suit):
                    # player who was last goes first in next round
                    player_order.append(player_order[i + 2])
                    player_order.append(player_order[i])
                    player_order.append(player_order[i + 1])
                else:
                    # player who was second goes first in next round
                    player_order.append(player_order[i + 1])
                    player_order.append(player_order[i + 2])
                    player_order.append(player_order[i])
            else:
                # player order stays the same
                player_order.append(player_order[i])
                player_order.append(player_order[i + 1])
                player_order.append(player_order[i + 2])
    return player_order


'''
:argument: suit which is trump
'''
# ToDo: can be merged with grand-function (for that: also change is_trump (?))
def order_suit(s):
    player_order = [1, 2, 3]

    for i in range(30):
        if i % 3 == 0:
            a = playedCards[i]
            b = playedCards[i + 1]
            c = playedCards[i + 2]

            value_a = compare_nonzero(a)
            if a.is_trump(s):
                value_a += 100

            value_b = compare_nonzero(b)
            if b.is_trump(s):
                value_b += 100

            value_c = compare_nonzero(c)
            if c.is_trump(s):
                value_c += 100

            if (value_b > value_a) and (a.suit == b.suit or b.is_trump(s)):
                if (value_c > value_b) and (a.suit == c.suit or c.is_trump(s)):
                    # player who was last goes first in next round
                    player_order.append(player_order[i + 2])
                    player_order.append(player_order[i])
                    player_order.append(player_order[i + 1])
                else:
                    # player who was second goes first in next round
                    player_order.append(player_order[i + 1])
                    player_order.append(player_order[i + 2])
                    player_order.append(player_order[i])
            else:
                # player order stays the same
                player_order.append(player_order[i])
                player_order.append(player_order[i + 1])
                player_order.append(player_order[i + 2])
    return player_order


'''
cards played sorted by player
'''
def create_player_lists():
    for i in range(30):
        match player_order[i]:
            case 1:
                hand_1.append(playedCards[i])
                continue
            case 2:
                hand_2.append(playedCards[i])
                continue
            case 3:
                hand_3.append(playedCards[i])
    ##########################################################################
    #print("hand of player 1: " + str(hand_1))
    #print("hand of player 2: " + str(hand_2))
    #print("hand of player 3: " + str(hand_3))
    #print(len(hand_1))
    ##########################################################################


def contains_equivalent(list, card, trump):
    if card.is_trump(trump):
        for c in list:
            if c.is_trump(trump):
                return True
    else:
        for c in list:
            if c.suit == card.suit:
                if trump != '0':        #  suit 'J' not allowed (except in zero game)
                    if c.suit != 'J':
                        return True
                    else:
                        return False
                else:
                    return True
    return False


def check_matching(s):
    boo = False
    for i in range(10):
        #if i % 3 == 0:
        first_player = player_order[i * 3]
        second_player = player_order[i * 3 + 1]
        third_player = player_order[i * 3 + 2]

        #first_card = playedCards[i * 3]
        #second_card = playedCards[i * 3 + 1]
        #third_card = playedCards[i * 3 + 2]
        match first_player:
            case 1:
                first_card = hand_1.pop(0)

                if contains_equivalent(hand_2, first_card, s):
                    second_card = hand_2.pop(0)
                    if contains_equivalent([second_card], first_card, s):
                        boo = True
                    else:
                        boo = False
                if contains_equivalent(hand_3, first_card, s):
                    third_card = hand_3.pop(0)
                    if contains_equivalent([third_card],first_card, s):
                        boo = True
                    else:
                        boo = False

            case 2:
                first_card = hand_2.pop(0)

                if contains_equivalent(hand_3, first_card, s):
                    second_card = hand_3.pop(0)
                    if contains_equivalent([second_card], first_card, s):
                        boo = True
                    else:
                        boo = False
                if contains_equivalent(hand_1, first_card, s):
                    second_card = hand_1.pop(0)
                    if contains_equivalent([third_card], first_card, s):
                        boo = True
                    else:
                        boo = False

            case 3:
                first_card = hand_3.pop(0)

                if contains_equivalent(hand_1, first_card, s):
                    second_card = hand_1.pop(0)
                    if contains_equivalent([second_card], first_card, s):
                        boo = True
                    else:
                        boo = False
                if contains_equivalent(hand_2, first_card, s):
                    second_card = hand_2.pop(0)
                    if contains_equivalent([third_card], first_card, s):
                        boo = True
                    else:
                        boo = False
    return boo


# ToDo: Check what needs to be considered with the last 2 cards not being dealt/played (cut off?)
# ToDo: move ordering functions to separate file
# ToDo: write test files


# 0 1 2 3 4 5 6 7 8 9


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filename = input("enter a filename: ")
    playedCards = read_file(filename)
    check = check_cardset(filename)
    if not check:
        print("not valid game; cardset incorrect")
        sys.exit()
    else:
        player_order = order_grand()
        #print(player_order)
        create_player_lists()
        #print(hand_1)
        grand = check_matching('G')
        if (grand):
            print("could have been a grand game")
        else:
            print("could not have been a grand game")
        hand_1 = []                                                # ToDo: might be possible to only write once
        hand_2 = []
        hand_3 = []

        player_order = order_zero()
        create_player_lists()
        zero = check_matching('0')
        if (zero):
            print("could have been a zero game")
        else:
            print("could not have been a zero game")
        hand_1 = []
        hand_2 = []
        hand_3 = []

        player_order = order_suit('D')
        create_player_lists()
        diamond = check_matching('D')
        if (diamond):
            print("could have been a diamond game")
        else:
            print("could not have been a diamond game")
        hand_1 = []
        hand_2 = []
        hand_3 = []

        player_order = order_suit('H')
        create_player_lists()
        heart = check_matching('H')
        if (heart):
            print("could have been a heart game")
        else:
            print("could not have been a heart game")
        hand_1 = []
        hand_2 = []
        hand_3 = []

        player_order = order_suit('S')
        create_player_lists()
        spade = check_matching('S')
        if (spade):
            print("could have been a spade game")
        else:
            print("could not have been a spade game")
        hand_1 = []
        hand_2 = []
        hand_3 = []

        player_order = order_suit('C')
        create_player_lists()
        club = check_matching('C')
        if (club):
            print("could have been a club game")
        else:
            print("could not have been a club game")
        hand_1 = []
        hand_2 = []
        hand_3 = []


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
