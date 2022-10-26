from Card import *


'''
argument: card object
returns: int, greater value beats lower value in game
'''
def compare_nonzero(c):
    match c.value:
        case '7':
            return 7
        case '8':
            return 8
        case '9':
            return 9
        case 'Q':
            return 10
        case 'K':
            return 11
        case '0':
            return 12
        case 'A':
            return 13
        case 'J':
            match c.suit:
                case 'D':
                    return 20
                case 'H':
                    return 21
                case 'S':
                    return 22
                case 'C':
                    return 23
                case _:
                    return 0

        case _:
            return 0

'''
argument: card object
returns: int, greater value beats lower value in game
'''
def compare_zero(c):
    match c.value:
        case '7':
            return 7
        case '8':
            return 8
        case '9':
            return 9
        case '0':
            return 10
        case 'J':
            return 11
        case 'Q':
            return 12
        case 'K':
            return 13
        case 'A':
            return 14



