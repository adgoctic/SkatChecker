# Copyright: Emil Obert, 2020
# Author:    Emil Obert <emil.obert@t-online.de>

# ToDo: add random card array generator for monte carlo analysis

class Card:
    def __init__(self, value = '', suit = ''):
        self.value = value
        self.suit = suit




class Checker:
    # cards = []
    def __init__(self, cardArray = []):
        self.cards = cardArray


    # takes 60(or less)-char string, converts to custom data type with attributes
    #   ->maybe change to list of 30 2-char strings(?)
    # !!!input syntax: value first, then suit (like english pronounciation)
    # returns: card array to be processed by checker class
    def convertForAlgorithm(input):
        #
        cardArray = []
        # create a Card object for every card and add it to array
        for index in enumerate(input):
            if index % 2 is 0:
                cardArray.append(Card(input[index], input[index + 1]))
            else:
                continue
        return cardArray



    # takes: gametype (represented by number (?))
    #       ToDo / idea: no argument, always all types, return all orders at once ( might add unneccesary runtime)
    # returns: array of 9 numbers, representing the relative position of starting player for every
    # round, first round is always player 1 (implicit, left out)
    def getOrder(self, gametype):
        player_order = []
        # switch case for game types (?)
        # outsource the 4 color options to another function ? (no quadruple code)
        # for zero game (no trump)
        if gametype is 0:
            dict_zero = {'7': 0,
                         '8': 1,
                         '9': 2,
                         '0': 3,
                         'J': 4,
                         'Q': 5,
                         'K': 6,
                         'A': 7}
            for i in range(9):
                # remember first-played card of this round
                first_card = self.cards[i * 3]
                suit_to_match = first_card.suit
                highest_value = dict_zero[first_card.value]

                # set 1st player as default for next starting player
                next_starting_player = 0  # offset ( either 0,1 or 2)
                next_card = self.cards[i * 3 + 1]

                # if suit matched and higher value (dict for comparison), update next starting player
                if (next_card.suit is suit_to_match) and (dict_zero[next_card.value] > highest_value):
                    next_starting_player = 1
                    highest_value = dict_zero[next_card.value]
                next_card = self.cards[i * 3 + 2]

                # repeat (not the most elegant solution?)
                if (next_card.suit is suit_to_match) and (dict_zero[next_card.value] > highest_value):
                    next_starting_player = 2
                    # highest_value = dict_zero[next_card.value]

                # note the next starting player, creating a list for the 2nd - 10th round in this game
                player_order.append(next_starting_player)





# if __name__ == '__main__':
