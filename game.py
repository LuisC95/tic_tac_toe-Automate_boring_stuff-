from main import status, confirmation
from board_update import board_update
from check_for_winners import check_for_winners
from switch_turns import switch_turns
from new_game import new_game_confirmation

def game_loop(player_in_turn, waiting_player): 
        while player_in_turn['current_status'] == status[0]: #while the current player is in 'playing' status
            try:
                move = int(input(f"\n {player_in_turn['name']} enter the number of position: "))

                match move:
                    #check if the move is valid (not already taken)
                    case move if move in waiting_player['moves'] or move in player_in_turn['moves'][:-1]: 
                        raise ValueError("Position already taken")
                    #check if the move is within the valid range
                    case move if move < 1 or move > 9: 
                        raise ValueError("Invalid input. Please enter a number between 1 and 9 corresponding to an empty position on the board.")
                    #check if the input is a number
                    case move if not str(move).isnumeric() and not isinstance(move, int): 
                        raise ValueError("Invalid input. Please enter a number between 1 and 9 corresponding to an empty position on the board.")
                
                player_in_turn['moves'].append(move) #add the player's move to their list of moves
                board_update(player_in_turn, player_in_turn['moves'][-1]) #update the board with the player's move

                total_moves = len(player_in_turn['moves']) + len(waiting_player['moves'])
                match total_moves:
                    case total_moves if total_moves < 9:
                        #check if the current player has won after making their move
                        if check_for_winners(player_in_turn): 
                            print(f"\n Current score: \n{player_in_turn['name']}'s score: {player_in_turn['score']} \n{waiting_player['name']}'s score: {waiting_player['score']}")
                            new_game_confirmation(confirmation, player_in_turn, waiting_player)
                        player_in_turn, waiting_player = switch_turns(player_in_turn, waiting_player) #switch turns between the current player and the waiting player   
                        pass
                    #check if the board is full and it's a draw 
                    case total_moves if total_moves == 9: 
                        raise ValueError(f"\nIt's a draw! The board is full. Starting a new game.")
                    case total_moves if total_moves == 9:
                        new_game_confirmation(confirmation, player_in_turn, waiting_player)
            except ValueError as e:
                print(e)
                pass