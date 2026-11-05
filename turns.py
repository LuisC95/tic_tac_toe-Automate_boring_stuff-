# The turn function determines which player's turn it is to play. 
# If both players have not made any moves yet, it randomly selects one of the players to start. 
# It updates the 'current_status' key in each player's dictionary to indicate who is playing and who is waiting. 
# Finally, it returns the player whose turn it is and their name.

import random
from symbols import status
from players import P1, P2


def take_turns(player_in_turn, player_waiting):
    # Determine which player should take the first turn if neither has a current status.
    while not P1['current_status'] and not P2['current_status']:            # Loop until one of the players has a current status set
        player_in_turn = random.choice([player_in_turn, player_waiting])    # Randomly select one of the players to start
        if player_in_turn == P1:    # If the selected player is P1, set them as active and P2 as waiting
            P1['current_status'] = status[0]                                
            P2['current_status'] = status[1]                                
            player_in_turn = P1                                             
            player_waiting = P2                                             
        else:                       # If the selected player is P2, set them as active and P1 as waiting
            P2['current_status'] = status[0]
            P1['current_status'] = status[1]
            player_in_turn = P2
            player_waiting = P1
        break
    if P1['current_status'] == 'playing' or P2['current_status'] == 'playing': # Loop while one of the players is active
        if P1['current_status'] == 'playing':            # If P1 is active, set them as the player in turn and P2 as waiting
            player_in_turn = P1
            player_waiting = P2
        elif P2['current_status'] == 'playing':          # If P2 is active, set them as the player in turn and P1 as waiting
            player_in_turn = P2
            player_waiting = P1

    return player_in_turn, player_waiting

def switch_turns(player_in_turn, waiting_player):
    #switch the current player and the waiting player
    if player_in_turn == P1:                # If the current player is P1, switch to P2
        P1['current_status'] = status[1]
        P2['current_status'] = status[0]
        player_in_turn = P2
        waiting_player = P1

    else:                                   # If the current player is P2, switch to P1
        P2['current_status'] = status[1]
        P1['current_status'] = status[0]
        player_in_turn = P1
        waiting_player = P2

    return player_in_turn, waiting_player

def is_only_one_playing(in_turn, waiting):
    # Validate the next turn by checking the current status of the players
    
    player_in_turn_playing = in_turn.get('current_status') == 'playing'
    player_waiting_playing = waiting.get('current_status') == 'playing'

    is_only_one_playing = player_in_turn_playing != player_waiting_playing

    if is_only_one_playing:
        return True
    raise ValueError("Invalid turn: both players are either active or inactive.")



    