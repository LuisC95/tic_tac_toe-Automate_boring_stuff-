from main import P1, P2, BLANK
from board import display_blank_board
from board import game_board

def reset_game():
    P1['moves'] = []
    P2['moves'] = []
    game_board['positions'] = [BLANK] * 9
    display_blank_board(BLANK)
    return P1['moves'], P2['moves'], game_board['positions']