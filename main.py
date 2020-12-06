# Copyright: Emil Obert, 2020
# Author:    Emil Obert <emil.obert@t-online.de>

#ToDo: add random card array generator for monte carlo analysis

class Card:
    def __init__(self, value = '', suit = ''):
        self.value = value
        self.suit = suit


# takes 60(or less)-char string, converts to custom data type with attributes
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


class Checker:
    cards = []
    def __init__(self, cardArray = []):
        self.cards = cardArray




if __name__ == '__main__':
    processUserInput('')