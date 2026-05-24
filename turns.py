# The turn function determines which player's turn it is to play. 
# If both players have not made any moves yet, it randomly selects one of the players to start. 
# It updates the 'current_status' key in each player's dictionary to indicate who is playing and who is waiting. 
# Finally, it returns the player whose turn it is and their name.

import random
from symbols import status
from players import P1, P2

def first_turn(player_in_turn, player_waiting ):

    while not P1['current_status'] and not P2['current_status']:
        player_in_turn = random.choice([P1, P2])
        if player_in_turn == P1:
            P1['current_status'] = status[0]
            P2['current_status'] = status[1]
            player_in_turn = P1
            player_waiting = P2

        else:
            P2['current_status'] = status[0]
            P1['current_status'] = status[1]
            player_in_turn = P2
            player_waiting = P1
        
    return player_in_turn, player_waiting

def switch_turns(player_in_turn, waiting_player):
    #switch the current player and the waiting player
    if player_in_turn == P1:
        P1['current_status'] = status[1]
        P2['current_status'] = status[0]
        player_in_turn = P2
        waiting_player = P1

    else:
        P2['current_status'] = status[1]
        P1['current_status'] = status[0]
        player_in_turn = P1
        waiting_player = P2

    return player_in_turn, waiting_player