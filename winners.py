win_conditions = [      [1,2,3], [4,5,6], [7,8,9], #rows
                        [1,4,7], [2,5,8], [3,6,9], #columns
                        [1,5,9], [3,5,7]] #diagonals

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

def claim_winner(player_in_turn, waiting_player):

    match player_in_turn['score'], waiting_player['score']:
        case player_score, waiting_score if player_score > waiting_score:
            print(f"\n{player_in_turn['name']} wins!".upper())
        case player_score, waiting_score if player_score == waiting_score:
            print("It's a tie!".upper())
        case player_score, waiting_score if player_score < waiting_score:
            print(f"\n{waiting_player['name']} wins!".upper())