#Tic Tac Toe Game
# players can be either X or O randomly assigned by name
# the game board is a 3x3 grid
# players take turns placing their symbol on the grid
# the first player to get three in a row wins

import random, time

#ALL_MOVES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
X, O, BLANK = 'X', 'O', ' ' #BLANK is used to represent an empty cell on the board
status = ['playing', 'waiting'] #'playing' indicates the player whose turn it is, while 'waiting' indicates the player who is waiting for their turn.

win_conditions = [      [1,2,3], [4,5,6], [7,8,9], #rows
                        [1,4,7], [2,5,8], [3,6,9], #columns
                        [1,5,9], [3,5,7]] #diagonals

game_board = {
    'positions': [],
    'panel': ''' 
 {} | {} | {}   1 | 2 | 3
 --+---+--   --+---+--
 {} | {} | {}   4 | 5 | 6
 --+---+--   --+---+--
 {} | {} | {}   7 | 8 | 9 ''',
} #list of valid positions on the board

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



# The assign_symbols function randomly assigns either 'X' or 'O' to player 1 and the other symbol to player 2. It updates the 'symbol' key in each player's dictionary and returns the assigned symbols for both players.
def assign_symbols():
    P1['symbol'] = random.choice([X, O])
    P2['symbol'] = O if P1['symbol'] == X else X
    return P1['symbol'], P2['symbol']

# The turn function determines which player's turn it is to play. If both players have not made any moves yet, it randomly selects one of the players to start. It updates the 'current_status' key in each player's dictionary to indicate who is playing and who is waiting. Finally, it returns the player whose turn it is and their name.
def first_turn(player_in_turn, player_waiting ):

    while not P1['current_status'] and not P2['current_status']:
        player_in_turn = random.choice([P1, P2])
        if player_in_turn == P1:
            P1['current_status'] = status[0]
            P2['current_status'] = status[1]
            player_in_turn = P1
            player_waiting = P2

        else:
            P2['current_status'] = status[0]
            P1['current_status'] = status[1]
            player_in_turn = P2
            player_waiting = P1
        
    return player_in_turn, player_waiting

def board_update(player_in_turn, position):
    #update the board with the player's symbol at the chosen position
    if not game_board['positions']:
        game_board['positions'] = [BLANK] * 9 #reset the board positions to blank before updating with the player's move

    game_board['positions'][player_in_turn['moves'][-1] - 1] = player_in_turn['symbol']

    print(game_board['panel'].format(*game_board['positions']))

    return player_in_turn['moves'], position, game_board['positions']
   
def switch_turns(player_in_turn, waiting_player):
    #switch the current player and the waiting player
    if player_in_turn == P1:
        P1['current_status'] = status[1]
        P2['current_status'] = status[0]
        player_in_turn = P2
        waiting_player = P1

    else:
        P2['current_status'] = status[1]
        P1['current_status'] = status[0]
        player_in_turn = P1
        waiting_player = P2

    return player_in_turn, waiting_player

def check_for_winners(player_in_turn):
    global is_there_a_winner
    #check if the current player has won by comparing their moves to the winning conditions
    is_there_a_winner = False
    player_moves = set(player_in_turn['moves']) #convert the player's moves to a set for easier comparison with the win conditions
    for condition in win_conditions:
        if set(condition).issubset(player_moves):
            print(f"{player_in_turn['name']} wins!")
            player_in_turn['score'] += 1
            is_there_a_winner = True
            break
    return  is_there_a_winner

    
def game_loop(player_in_turn, waiting_player):

    
        while player_in_turn['current_status'] == status[0]: #while the current player is in 'playing' status
            try:
                move = int(input(f"enter the number corresponding to the position on the board where you want to place your symbol: "))

                if move in waiting_player['moves']or move in player_in_turn['moves'][:-1]: #check if the move is valid (not already taken)
                    raise ValueError("Position already taken")
                if move < 1 or move > 9: #check if the move is within the valid range
                    raise ValueError("Invalid input. Please enter a number between 1 and 9 corresponding to an empty position on the board.")
                if len(game_board['positions']) > 9: #check if the board is full
                    raise ValueError("The board is full. It's a draw!")
                
                player_in_turn['moves'].append(move) #add the player's move to their list of moves
                board_update(player_in_turn, player_in_turn['moves'][-1]) #update the board with the player's move

                if check_for_winners(player_in_turn): #check if the current player has won after making their move
                    print(f"{player_in_turn['name']} wins!")
                    player_in_turn['score'] += 1
                    break
                #game_board['positions'][player_in_turn['moves'][-1] - 1] = player_in_turn['symbol'] #update the game board positions with the player's symbol
                player_in_turn, waiting_player = switch_turns(player_in_turn, waiting_player) #switch turns between the current player and the waiting player
                pass
                check_for_winners(player_in_turn) #check if the current player has won after making their move
            except ValueError as e:
                print(e)
                pass
    
    
             


# The display_blank_board function prints the initial state of the tic tac toe board, which is empty. It also provides instructions to the players on how to make a move by entering the corresponding number for the position on the board where they want to place their symbol. The board is displayed using the BOARD variable, with all positions filled with the BLANK symbol.
def display_blank_board(space):
    space_board = [space] * 9
    print('instructions: To make a move, enter the number corresponding to the position on the board where you want to place your symbol.')
    print(game_board['panel'].format(*space_board))  
    

def main():
    
    active_player = ''
    pasive_player = ''
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
