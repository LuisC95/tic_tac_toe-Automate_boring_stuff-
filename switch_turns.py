from main import P1, P2, status

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