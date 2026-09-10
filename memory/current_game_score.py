# On this document, I will create the logic to keep track of the current game score.
# The score will be updated each time a player wins, and it will be displayed at the end of each game.
# The score will be stored in the 'score' key of each player's dictionary, and it
#at the end of the game, the scores will be updated to global score variable to keep track of the overall score of both players throughout multiple games.

from players import P1, P2

def save_current_game_score(winner):
    if winner == "Player 1":
        P1['score'] += 1
    elif winner == "Player 2":
        P2['score'] += 1