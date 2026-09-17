win_conditions = [      [1,2,3], [4,5,6], [7,8,9], #rows
                        [1,4,7], [2,5,8], [3,6,9], #columns
                        [1,5,9], [3,5,7]] #diagonals

def check_for_winners(player_in_turn, waiting_player):
    #check if the current player has won by comparing their moves to the winning conditions
    #convert the player's moves to a set for easier comparison with the win conditions
    player_moves = set(player_in_turn['moves']) 
    is_there_a_winner = False
    for condition in win_conditions:
        if set(condition).issubset(player_moves):
            print(f"\n{player_in_turn['name']} wins!")
            player_in_turn['game_status'] = 'Win'
            waiting_player['game_status'] = 'Loss'
            is_there_a_winner = True
            break
    return  True if is_there_a_winner else False

def percentage_calculation(player):
    #calculate score percentages: wins, losses and ties
    player['win_percentage'] = round(float((player['won_games'] / player['games_played'])*100), 2)
    player['lost_percentage'] = round(float((player['lost_games'] / player['games_played'])*100), 2)
    player['tied_percentage'] = round(float((player['tied_games']/player['games_played'])*100), 2)
    return player['win_percentage'], player['lost_percentage'], player['tied_percentage']

def reset_game_status(player_in_turn, waiting_player):
    #reset the game status for both players 
    player_in_turn['game_status'] = 'Tie'
    waiting_player['game_status'] = 'Tie'
    return player_in_turn['game_status'], waiting_player['game_status']

def record_scores(result, player_in_turn, waiting_player):
    #record the scores based on the result of the game
    player_in_turn['games_played'] += 1
    waiting_player['games_played'] += 1

    match result:
        case 'Win':
            player_in_turn['score'] += 1
            player_in_turn['won_games'] += 1
            waiting_player['lost_games'] += 1
        case 'Loss':
            waiting_player['score'] += 1
            waiting_player['won_games'] += 1
            player_in_turn['lost_games'] += 1
        case 'Tie':
            player_in_turn['tied_games'] += 1
            waiting_player['tied_games'] += 1
        case _:
            raise ValueError(f"Invalid result: {result}")

    return player_in_turn['score'], waiting_player['score']

def scores_updating(player_in_turn, waiting_player):
    # update the player's average score, win, loss, and games played
    while player_in_turn['game_status'] == 'Win' or  player_in_turn['game_status'] == 'Tie':
            record_scores(player_in_turn['game_status'],player_in_turn, waiting_player)
            percentage_calculation(player_in_turn)
            percentage_calculation(waiting_player)
            break

    reset_game_status(player_in_turn, waiting_player)

def claim_winner(player_in_turn, waiting_player):

    match player_in_turn['score'], waiting_player['score']:
        case player_score, waiting_score if player_score > waiting_score:
            print(f"\n{player_in_turn['name']} wins!".upper())
            print(f'\n Average per game: {player_in_turn["name"]}: \n   wins {player_in_turn["win_percentage"]}%\n   losses {player_in_turn["lost_percentage"]}\n   tied games {player_in_turn["tied_percentage"]}%\n{waiting_player["name"]} won: {waiting_player["win_percentage"]}% of the times')
        case player_score, waiting_score if player_score == waiting_score:
            print("It's a tie!".upper())
            print(f'\n Average per game: {player_in_turn["name"]}: \n   wins {player_in_turn["win_percentage"]}%\n   losses {player_in_turn["lost_percentage"]}\n   tied games {player_in_turn["tied_percentage"]}%\n{waiting_player["name"]} won: {waiting_player["win_percentage"]}% of the times')
        case player_score, waiting_score if player_score < waiting_score:
            print(f"\n{waiting_player['name']} wins!".upper())
            print(f'\n Average per game: {player_in_turn["name"]}: \n   wins {player_in_turn["win_percentage"]}%\n   losses {player_in_turn["lost_percentage"]}\n   tied games {player_in_turn["tied_percentage"]}%\n{waiting_player["name"]}: \n   wins {waiting_player["win_percentage"]}%\n   losses {waiting_player["lost_percentage"]}\n   tied games {waiting_player["tied_percentage"]}%')
            print(f'\n Losing average per game: {player_in_turn["name"]}: {player_in_turn["win_percentage"]}% of the times')
