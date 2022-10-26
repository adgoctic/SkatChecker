class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    '''
    :argument: card object c, trump suit
    '''
    def is_trump(self, trump):
        if trump == '0':  # ignore this function in zero-game (relevant when called from check_matching)
            return False
        else:
            return (self.value == 'J' or self.suit == trump)

    #def to_string(self):
    #    return self.suit + self.value

    def __eq__(self, other):
        return (self.value == other.value and self.suit == other.suit)

    def __hash__(self):
        return hash((self.suit, self.value))

    def __repr__(self):
        return self.suit + self.value