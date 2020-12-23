# Copyright: Emil Obert, 2020
# Author:    Emil Obert <emil.obert@t-online.de>

# ToDo: add random card array generator for monte carlo analysis

class Card:
    def __init__(self, value = '', suit = ''):
        self.value = value
        self.suit = suit




class Checker:
    cards = []
    def __init__(self, cardArray = []):
        self.cards = cardArray


    # takes 60(or less)-char string, converts to custom data type with attributes
    #   ->maybe change to list of 30 2-char strings(?)
    # !!!input syntax: value first, then suit (like english pronounciation)
    # returns: card array to be processed by checker class
    def processUserInput(input):
        #
        cardArray = []
        # create a Card object for every card and add it to array
        for index in enumerate(input):
            if index % 2 is 0:
                cardArray.append(Card(input[index], input[index + 1]))
            else:
                continue
        return cardArray

    # takes: gametype (ToDo: represent by number (?)
    #       ToDo / idea: no argument, always all types, return all orders at once ( might add unneccesary runtime)
    # returns: array of 9 numbers, representing the relative position of starting player for every
    # round, first round is always player 1 (implicit, left out)
    def getOrder(gametype):
        # switch case for game types (?)
        # outsource the 4 color options to another function ? (no quadruple code)



# if __name__ == '__main__':
