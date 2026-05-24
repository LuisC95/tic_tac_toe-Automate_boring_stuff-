
# The assign_symbols function randomly assigns either 'X' or 'O' to player 1 and the other symbol to player 2. 
# It updates the 'symbol' key in each player's dictionary and returns the assigned symbols for both players.

import random
from players import P1, P2

X, O, BLANK = 'X', 'O', ' ' #BLANK is used to represent an empty cell on the board
status = ['playing', 'waiting'] #'playing' indicates the player whose turn it is, while 'waiting' indicates the player who is waiting for their turn.
confirmation = None


def assign_symbols():
    P1['symbol'] = random.choice([X, O])
    P2['symbol'] = O if P1['symbol'] == X else X
    return P1['symbol'], P2['symbol']