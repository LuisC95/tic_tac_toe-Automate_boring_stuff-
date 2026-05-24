from main import BLANK

game_board = {
    'positions': [],
    'panel': ''' 
 {} | {} | {}   1 | 2 | 3
 --+---+--   --+---+--
 {} | {} | {}   4 | 5 | 6
 --+---+--   --+---+--
 {} | {} | {}   7 | 8 | 9 '''.center(50),
} #list of valid positions on the board


def board_update(player_in_turn, position):
    #update the board with the player's symbol at the chosen position
    if not game_board['positions']:
        #reset the board positions to blank before updating with the player's move
        game_board['positions'] = [BLANK] * 9 

    game_board['positions'][player_in_turn['moves'][-1] - 1] = player_in_turn['symbol']
    print(game_board['panel'].format(*game_board['positions']))
    return player_in_turn['moves'], position, game_board['positions']
   

# The display_blank_board function prints the initial state of the tic tac toe board, which is empty. It also provides instructions to the players on how to make a move by entering the corresponding number for the position on the board where they want to place their symbol. The board is displayed using the BOARD variable, with all positions filled with the BLANK symbol.
def display_blank_board(space):
    space_board = [space] * 9
    print('instructions: To make a move, enter the number corresponding to the position on the board where you want to place your symbol.')
    print(game_board['panel'].format(*space_board))