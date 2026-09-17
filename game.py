from players import P1, P2
from board import board_update, display_blank_board, game_board
from winners import check_for_winners, claim_winner, scores_updating
from turns import switch_turns
from symbols import status, BLANK
# from memory.global_score import global_score_update, average_score_calculation

import sys


def new_game_confirmation(confirmation,player_in_turn, waiting_player):
    # Ask the players if they want to start a new game
    while True:
        new_game = input("Do you want to play again? (y/n): ").lower()
        confirmation = None
        if new_game == 'y':
            reset_game()
        else:
            claim_winner(player_in_turn, waiting_player)
            #global_score_update(player_in_turn, waiting_player)
            sys.exit("Thanks for playing!")
        return confirmation
    

def reset_game():
    # Reset the game state for a new game
    P1['moves'] = []
    P2['moves'] = []
    game_board['positions'] = [BLANK] * 9
    display_blank_board(BLANK)
    return P1['moves'], P2['moves'], game_board['positions']

def move_validation(occupied_positions, move):
     # Validate the player's move before accepting it
    match move:
        #check if the move is valid (not already taken)
        case move if move in occupied_positions: 
            raise ValueError("Position already taken")
        #check if the move is within the valid range
        case move if move < 1 or move > 9: 
            raise ValueError("Invalid input. Please enter a number between 1 and 9 corresponding to an empty position on the board.")



def game_loop(player_in_turn, waiting_player): 
        
        confirmation = None
        while player_in_turn['current_status'] == status[0]:  
            # Continue until the current player is no longer in 'playing' status
            try:
                move = int(input(f"\n {player_in_turn['name']} enter the number of position: "))
                move_validation(waiting_player['moves'] + player_in_turn['moves'], move)
                player_in_turn['moves'].append(move) #add the player's move to their list of moves

                board_update(player_in_turn, player_in_turn['moves'][-1]) #update the board with the player's move

                

                total_moves = len(player_in_turn['moves']) + len(waiting_player['moves'])
                match total_moves:
                    case total_moves if total_moves <= 9:
                    #check if the current player has won after making their move
                        if check_for_winners(player_in_turn, waiting_player):
                            scores_updating(player_in_turn, waiting_player)
                            #average_score_calculation(player_in_turn)
                            #average_score_calculation(waiting_player)
                            print(f"\n  Current score: \n{player_in_turn['name']}'s score: {player_in_turn['score']} \n{waiting_player['name']}'s score: {waiting_player['score']}")
                            print(f'\n  Average per game: \n{player_in_turn["name"]}: \n  wins: {player_in_turn["win_percentage"]}% \n  losses: {player_in_turn["lost_percentage"]}% \n  tied games: {player_in_turn["tied_percentage"]}%\n{waiting_player["name"]}: \n  wins: {waiting_player["win_percentage"]}% \n  losses: {waiting_player["lost_percentage"]}% \n  tied games: {waiting_player["tied_percentage"]}%')
                            
                            new_game_confirmation(confirmation, player_in_turn, waiting_player)
                            
                        elif total_moves == 9 and not check_for_winners(player_in_turn, waiting_player): 
                            #if the board is full and there is no winner, it's a draw
                            print("\n It's a draw!")
                            scores_updating(player_in_turn, waiting_player)
                            #average_score_calculation(player_in_turn)
                            #average_score_calculation(waiting_player)
                            print(f"\n  Current score: \n{player_in_turn['name']}'s score: {player_in_turn['score']} \n{waiting_player['name']}'s score: {waiting_player['score']}")
                            print(f'\n  Average per game: \n\n{player_in_turn["name"]}: \n  wins: {player_in_turn["win_percentage"]}% \n  losses: {player_in_turn["lost_percentage"]}% \n  tied games: {player_in_turn["tied_percentage"]}%\n{waiting_player["name"]}: \n  wins: {waiting_player["win_percentage"]}% \n  losses: {waiting_player["lost_percentage"]}% \n  tied games: {waiting_player["tied_percentage"]}%')
                            new_game_confirmation(confirmation, player_in_turn, waiting_player)
                        player_in_turn, waiting_player = switch_turns(player_in_turn, waiting_player) #switch turns between the current player and the waiting player   
                        pass
            except ValueError as e:
                print(e)
