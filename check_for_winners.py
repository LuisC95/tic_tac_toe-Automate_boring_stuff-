from main import win_conditions

def check_for_winners(player_in_turn):
    #check if the current player has won by comparing their moves to the winning conditions
    global is_there_a_winner
    is_there_a_winner = False


    #convert the player's moves to a set for easier comparison with the win conditions
    player_moves = set(player_in_turn['moves']) 
    for condition in win_conditions:
        if set(condition).issubset(player_moves):
            print(f"\n{player_in_turn['name']} wins!")
            player_in_turn['score'] += 1
            is_there_a_winner = True
            break
    return  is_there_a_winner