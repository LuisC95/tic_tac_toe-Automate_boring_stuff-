from reset_game import reset_game
from claim_winner import claim_winner
import sys

def new_game_confirmation(confirmation,player_in_turn, waiting_player):
    
    while True:
        new_game = input("Do you want to play again? (y/n): ").lower()
        confirmation = None
        if new_game == 'y':
            reset_game()
        else:
            claim_winner(player_in_turn, waiting_player)
            sys.exit("Thanks for playing!")
        return confirmation