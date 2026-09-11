#Tic Tac Toe Game
# players can be either X or O randomly assigned by name
# the game board is a 3x3 grid
# players take turns placing their symbol on the grid
# the first player to get three in a row wins

from symbols import assign_symbols
from turns import first_turn
from board import display_blank_board
from game import game_loop
from symbols import BLANK
from players import P1, P2
#from memory.global_score import average_score_calculation


def get_valid_player_name(prompt):
    # Get player names from input and validate them
    while True:
        name = input(prompt).strip()
        if not name:
            print("Name cannot be empty. Please try again.")
        else:
            return name

def main():
    print("Welcome to Tic Tac Toe!")
    P1['name'] = get_valid_player_name("Player 1, please enter your name: ")
    P2['name'] = get_valid_player_name("Player 2, please enter your name: ")
    active_player = {}
    pasive_player = {}


    assign_symbols()
    active_player, pasive_player = first_turn(active_player, pasive_player)

    print(f"{P1['name']} is {P1['symbol']} and {P2['name']} is {P2['symbol']}.") 

    display_blank_board(BLANK)
    print(f'\n {active_player["name"]} will go first.')
    game_loop(active_player, pasive_player)

if __name__ == "__main__":
    main()
