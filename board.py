from board import game_board

game_board = {
    'positions': [],
    'panel': ''' 
 {} | {} | {}   1 | 2 | 3
 --+---+--   --+---+--
 {} | {} | {}   4 | 5 | 6
 --+---+--   --+---+--
 {} | {} | {}   7 | 8 | 9 '''.center(50),
} #list of valid positions on the board

# The display_blank_board function prints the initial state of the tic tac toe board, which is empty. It also provides instructions to the players on how to make a move by entering the corresponding number for the position on the board where they want to place their symbol. The board is displayed using the BOARD variable, with all positions filled with the BLANK symbol.
def display_blank_board(space):
    space_board = [space] * 9
    print('instructions: To make a move, enter the number corresponding to the position on the board where you want to place your symbol.')
    print(game_board['panel'].format(*space_board))