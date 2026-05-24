
# The assign_symbols function randomly assigns either 'X' or 'O' to player 1 and the other symbol to player 2. 
# It updates the 'symbol' key in each player's dictionary and returns the assigned symbols for both players.

import random
from main import P1, P2, X, O

def assign_symbols():
    P1['symbol'] = random.choice([X, O])
    P2['symbol'] = O if P1['symbol'] == X else X
    return P1['symbol'], P2['symbol']