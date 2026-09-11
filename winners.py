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
            player_in_turn['last_game_winner'] = True
            is_there_a_winner = True
            break
    return  is_there_a_winner


def scores_updating(player_in_turn, waiting_player):
    # update the player's average score, win, loss, and games played
    while True or not player_in_turn['last_game_winner']:
        if player_in_turn['last_game_winner'] == True:
            
            player_in_turn['won_games'] += 1
            player_in_turn['games_played'] += 1

            waiting_player['lost_games'] += 1
            waiting_player['games_played'] += 1
            
            
            player_in_turn['won_percentage'] = round(float((player_in_turn['won_games'] / player_in_turn['games_played'])*100), 2)
            player_in_turn['lost_percentage'] = round(float((player_in_turn['lost_games'] / player_in_turn['games_played'])*100), 2)

            waiting_player['won_percentage'] = round(float((waiting_player['won_games'] / waiting_player['games_played'])*100), 2)
            waiting_player['tied_percentage'] = round(float((waiting_player['tied_games']/waiting_player['games_played'])*100), 2)
            waiting_player['lost_percentage'] = round(float((waiting_player['lost_games'] / waiting_player['games_played'])*100), 2)       

        elif player_in_turn['last_game_winner'] == False:

            player_in_turn['games_played'] += 1
            player_in_turn['lost_games'] += 1
            player_in_turn['lost_percentage'] = round(float((player_in_turn['lost_games'] / player_in_turn['games_played'])*100), 2)

            waiting_player['won_games'] += 1
            waiting_player['games_played'] += 1
            waiting_player['games_played'] += 1

            waiting_player['won_percentage'] = round(float((waiting_player['won_games']) / waiting_player['games_played'])*100, 2)
            waiting_player['lost_percentage'] = round(float((waiting_player['lost_games'] / waiting_player['games_played'])*100), 2)
            waiting_player['tied_percentage'] = round(float((waiting_player['tied_games']/waiting_player['games_played'])*100), 2)

            player_in_turn['won_percentage'] = round(float((player_in_turn['won_games'] / player_in_turn['games_played'])*100), 2)
            player_in_turn['tied_percentage'] = round(float((player_in_turn['tied_games']/player_in_turn['games_played'])*100), 2)
            player_in_turn['lost_percentage'] = round(float(((player_in_turn['games_played'] - player_in_turn['lost_games']- player_in_turn['won_games']) / player_in_turn['games_played'])*100), 2)

        else:
            player_in_turn['games_played'] += 1
            player_in_turn['tied_games'] += 1
            player_in_turn['won_percentage'] = round(float((player_in_turn['won_games'] / player_in_turn['games_played'])*100), 2)
            player_in_turn['lost_percentage'] = round(float((player_in_turn['lost_games'] / player_in_turn['games_played'])*100), 2)
            player_in_turn['tied_percentage'] = round(float((player_in_turn['tied_games']/player_in_turn['games_played'])*100), 2)

            waiting_player['games_played'] += 1
            waiting_player['tied_games'] += 1
            waiting_player['won_percentage'] = round(float((waiting_player['won_games']  / waiting_player['games_played'])*100), 2)
            waiting_player['lost_percentage'] = round(float((waiting_player['lost_games'] / waiting_player['games_played'])*100), 2)
            waiting_player['tied_percentage'] = round(float((waiting_player['tied_games']/waiting_player['games_played'])*100), 2)
        break

    player_in_turn['last_game_winner'] = None
    waiting_player['last_game_winner'] = None

def claim_winner(player_in_turn, waiting_player):

    match player_in_turn['score'], waiting_player['score']:
        case player_score, waiting_score if player_score > waiting_score:
            print(f"\n{player_in_turn['name']} wins!".upper())
            print(f'\n Average per game: {player_in_turn["name"]}: \n   wins {player_in_turn["won_percentage"]}%\n   losses {player_in_turn["lost_percentage"]}\n   tied games {player_in_turn["tied_percentage"]}%\n{waiting_player["name"]} won: {waiting_player["won_percentage"]}% of the times')
        case player_score, waiting_score if player_score == waiting_score:
            print("It's a tie!".upper())
            print(f'\n Average per game: {player_in_turn["name"]}: \n   wins {player_in_turn["won_percentage"]}%\n   losses {player_in_turn["lost_percentage"]}\n   tied games {player_in_turn["tied_percentage"]}%\n{waiting_player["name"]} won: {waiting_player["won_percentage"]}% of the times')
        case player_score, waiting_score if player_score < waiting_score:
            print(f"\n{waiting_player['name']} wins!".upper())
            print(f'\n Average per game: {player_in_turn["name"]}: \n   wins {player_in_turn["won_percentage"]}%\n   losses {player_in_turn["lost_percentage"]}\n   tied games {player_in_turn["tied_percentage"]}%\n{waiting_player["name"]}: \n   wins {waiting_player["won_percentage"]}%\n   losses {waiting_player["lost_percentage"]}\n   tied games {waiting_player["tied_percentage"]}%')
            print(f'\n Losing average per game: {player_in_turn["name"]}: {player_in_turn["won_percentage"]}% of the times')
