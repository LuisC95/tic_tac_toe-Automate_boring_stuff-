#Tic Tac Toe Game
# players can be either X or O randomly assigned by name
# the game board is a 3x3 grid
# players take turns placing their symbol on the grid
# the first player to get three in a row wins

from symbols import assign_symbols
from turns import take_turns
from board import display_blank_board, display_current_board
from game import game_loop
from symbols import BLANK
from players import P1, P2
from save_game import saved_games_list
from game import load_game, exit_game
from symbols import status
from board import game_board
import os
#from memory.global_score import average_score_calculation


def get_valid_player_name(prompt):
    # Get player names from input and validate them
    while True:
        name = input(prompt).strip()
        if not name:
            print("Name cannot be empty. Please try again.")
        else:
            return name

def main_menu():
    print("Welcome to the Tic Tac Toe Main Menu!")
    print(f"\n1. Start a new game")
    print(f"2. Load a saved game")
    print(f"3. Exit")
    choice = int(input(f"\nEnter your choice (1, 2, or 3): "))
                 

    match choice:
        case choice if choice == 1:
            P1['name'] = get_valid_player_name("Player 1, please enter your name: ")
            P2['name'] = get_valid_player_name("Player 2, please enter your name: ")
        case 2:
            saved_games = []
            saved_games = saved_games_list(saved_games)
            print(saved_games)
            if not saved_games:
                raise ValueError("No saved games found.")
            else:
                print(f"\nSaved games:")
                for i, game in enumerate(saved_games, start=1):
                    print(f"{i}. {game}")
                choice = int(input(f"\nchoose a game to load by entering its number: "))
                if 1 <= choice <= len(saved_games):
                    load_game(saved_games[choice - 1])
                else:
                    raise ValueError(f"\nInvalid choice.")
                    
        case 3: 
            exit_game()
        case _:
            print("Invalid choice. Please try again.")
            main_menu()


def active_and_pasive_players_validation(active_player, pasive_player):
    # Validate the active and pasive players based on their current status
    # If either player does not have a current status, determine the first turn
    
    if P1['current_status'] == 'playing':
        active_player = P1
        pasive_player = P2
        return P1, P2
    elif P2['current_status'] == 'playing':
        active_player = P2
        pasive_player = P1
        return active_player, pasive_player
    else:
        return active_player, pasive_player

def main():
    main_menu()
    active_player = {}
    pasive_player = {}
    
    active_player, pasive_player = active_and_pasive_players_validation(active_player, pasive_player)
    active_player['current_status'] = status[0]
    pasive_player['current_status'] = status[1]
    take_turns(active_player, pasive_player)


    assign_symbols()

    print(f"{P1['name']} is {P1['symbol']} and {P2['name']} is {P2['symbol']}.") 

    if not game_board['positions']:
        display_blank_board(BLANK)
        print(f'\n {active_player["name"]} will go first.')
        game_loop(active_player, pasive_player)
    else:
        display_current_board()
        game_loop(active_player, pasive_player)

if __name__ == "__main__":
    main()
