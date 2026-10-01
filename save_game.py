import os 
from players import P1, P2
from game import game_board
from datetime import datetime

current_game_status = {
    'positions': game_board['positions'],
    'p1_moves': P1['moves'],
    'p2_moves': P2['moves'],
    'current_turn': 'P1' if len(P1['moves']) <= len(P2['moves']) else 'P2',
    'p1_current_game': [P1['won_games'], P1['lost_games'],P1['tied_games'], P1['score'],  P1['average'], P1['name']],
    'p2_current_game': [P2['won_games'], P2['lost_games'], P2['tied_games'], P2['score'], P2['average'], P2['name']]
}

def name_for_save_file(game_name):
    input_name = input(f"Enter the name for the save file for {game_name['name']} (leave blank for default): ")
    input_date=f"_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    if input_name:
        return input_name + input_date + ".txt"
    if not input_name:
        input_name = f"save{input_date}.txt"
    return input_name + input_date + ".txt"

def save_game(status, route):                                   # Extract the current game status from the status dictionary
    
    positions = status['positions']                             # 9 positions on the game board
    p1_moves = status['p1_moves']                               # moves made by player 1
    p2_moves = status['p2_moves']                               # moves made by player 2
    p1_game_stats = current_game_status['p1_current_game']
    p2_game_stats = current_game_status['p2_current_game']

    line_positions = '|'.join(positions)                        # 3x3 game board positions
    line_p1 = ','.join(str(m) for m in p1_moves)                # list of moves made by player 1
    line_p2 = ','.join(str(m) for m in p2_moves)                # list of moves made by player 2

    with open(route, 'w') as f:                                 # Open the save file for writing
        f.write(line_positions + '\n')
        f.write(line_p1 + '\n')
        f.write(line_p2 + '\n')
        f.write(','.join(str(m) for m in p1_game_stats) + '\n')
        f.write(','.join(str(m) for m in p2_game_stats) + '\n')

def load_game(route):                                           # Load the game status from the save file
    if not os.path.exists(route):                               # Check if the save file exists
        return None                                             # save file does not exist
    
    with open(route) as f:                                      # Open the save file for reading
        lines = f.read().splitlines()

    line_posiciones = lines[0]                                  # 3x3 game board positions
    line_p1 = lines[1]                                          # list of moves made by player 1
    line_p2 = lines[2]                                          # list of moves made by player 2
    line_p1_game_stats = lines[3]                               # player 1 game stats
    line_p2_game_stats = lines[4]                               # player 2 game stats

    positions = line_posiciones.split('|')                      # 3x3 game board positions
    p1_moves = [int(m) for m in line_p1.split(',') if m != '']  # list of moves made by player 1
    p2_moves = [int(m) for m in line_p2.split(',') if m != '']  # list of moves made by player 2

    P1['won_games'] = int(line_p1_game_stats.split(',')[0])
    P1['lost_games'] = int(line_p1_game_stats.split(',')[1])
    P1['tied_games'] = int(line_p1_game_stats.split(',')[2])
    P1['score'] = int(line_p1_game_stats.split(',')[3])

    P1['average'] = int(line_p1_game_stats.split(',')[4])
    P1['name'] = line_p1_game_stats.split(',')[5]
    P2['won_games'] = int(line_p2_game_stats.split(',')[0])
    P2['lost_games'] = int(line_p2_game_stats.split(',')[1])
    P2['tied_games'] = int(line_p2_game_stats.split(',')[2])
    P2['score'] = int(line_p2_game_stats.split(',')[3])
    P2['average'] = int(line_p2_game_stats.split(',')[4])
    P2['name'] = line_p2_game_stats.split(',')[5]
    
    return {
        'positions': positions,
        'p1_moves': p1_moves,
        'p2_moves': p2_moves,
        'p1_current_game': [int(m) for m in line_p1_game_stats.split(',') if m != ''],
        'p2_current_game': [int(m) for m in line_p2_game_stats.split(',') if m != ''],
        'p1_name': P1['name'],
        'p2_name': P2['name'],
        'p1_won_games': P1['won_games'],
        'p1_lost_games': P1['lost_games'],
        'p1_tied_games': P1['tied_games'],
        'p1_score': P1['score'],
        'p1_average': P1['average'],
        'p2_won_games': P2['won_games'],
        'p2_lost_games': P2['lost_games'],
        'p2_tied_games': P2['tied_games'],
        'p2_score': P2['score'],
        'p2_average': P2['average']
    
    }

    