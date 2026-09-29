import os 

def save_game(status, route):
    # Extract the current game status from the status dictionary
    
    positions = status['positions']                     # 9 positions on the game board
    p1_moves = status['p1_moves']                       # moves made by player 1
    p2_moves = status['p2_moves']                       # moves made by player 2

    line_positions = '|'.join(positions)                # 3x3 game board positions
    line_p1 = ','.join(str(m) for m in p1_moves)        # list of moves made by player 1
    line_p2 = ','.join(str(m) for m in p2_moves)        # list of moves made by player 2

    with open(route, 'w') as f:
        f.write(line_positions + '\n')
        f.write(line_p1 + '\n')
        f.write(line_p2 + '\n')

def load_game(route):                                   # Load the game status from the save file
    if not os.path.exists(route):                       # Check if the save file exists
        return None                                     #save file does not exist
    
    with open(route) as f:                              # Open the save file for reading
        lines = f.read().splitlines()

    line_posiciones = lines[0]                          # 3x3 game board positions
    line_p1 = lines[1]                                  # list of moves made by player 1
    line_p2 = lines[2]                                  # list of moves made by player 2

    positions = line_posiciones.split('|')
    p1_moves = [int(m) for m in line_p1.split(',') if m != '']
    p2_moves = [int(m) for m in line_p2.split(',') if m != '']

    return {
        'positions': positions,
        'p1_moves': p1_moves,
        'p2_moves': p2_moves,
    }