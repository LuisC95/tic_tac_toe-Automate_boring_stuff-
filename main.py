#Tic Tac Toe Game
# players can be either X or O randomly assigned by name
# the game board is a 3x3 grid
# players take turns placing their symbol on the grid
# the first player to get three in a row wins

from assign_symbols import assign_symbols
from turns import first_turn
from board import display_blank_board
from game import game_loop

X, O, BLANK = 'X', 'O', ' ' #BLANK is used to represent an empty cell on the board
status = ['playing', 'waiting'] #'playing' indicates the player whose turn it is, while 'waiting' indicates the player who is waiting for their turn.
confirmation = None

win_conditions = [      [1,2,3], [4,5,6], [7,8,9], #rows
                        [1,4,7], [2,5,8], [3,6,9], #columns
                        [1,5,9], [3,5,7]] #diagonals

P1 = { #dictionary to store player 1's information
    'symbol': [],
    'moves': [],
    'current_status': [],
    'score': 0
}

P2 = { #dictionary to store player 2's information
    'symbol': [],
    'moves': [],
    'current_status': [],
    'score': 0
}

def main():
    
    active_player = {}
    pasive_player = {}
    print("Welcome to Tic Tac Toe!")
    P1.setdefault('name', input("Player 1, please enter your name: "))
    P2.setdefault('name', input("Player 2, please enter your name: "))

    assign_symbols()
    active_player, pasive_player = first_turn(active_player, pasive_player)

    print(f"{P1['name']} is {P1['symbol']} and {P2['name']} is {P2['symbol']}.") 

    display_blank_board(BLANK)
    print(f'\n {active_player["name"]} will go first.')
    game_loop(active_player, pasive_player)

if __name__ == "__main__":
    main()
