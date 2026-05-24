
from board import game_board
from main import BLANK

def board_update(player_in_turn, position):
    #update the board with the player's symbol at the chosen position
    if not game_board['positions']:
        game_board['positions'] = [BLANK] * 9 #reset the board positions to blank before updating with the player's move

    game_board['positions'][player_in_turn['moves'][-1] - 1] = player_in_turn['symbol']

    print(game_board['panel'].format(*game_board['positions']))

    return player_in_turn['moves'], position, game_board['positions']
   