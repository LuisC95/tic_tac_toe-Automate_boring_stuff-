# On this document, Im will create the global score variable and the function to update it. 
# The score will be updated based on the number of winning combinations a player has achieved. 
# Each time a player wins, their score will increase by 1. 
# The global score variable will be used to keep track of the scores of both players throughout the game.

from players import P1, P2

def global_score_reading():
        with open('global_score.txt', "r") as global_score :
            pass
pass

def global_score_update( player_in_turn, waiting_player):
     with open('global_score.txt', 'w') as global_score:

        pass

pass


top_scoreboard = {
    'player_name': {P1['name'], P2['name']},
    'top_position': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'average': {P1['average'], P2['average']}

}

'''def average_score_calculation(player):
    if player['won_games'] > 0:
        player['average'] = int(player['score'] / player['won_games'])
    else:
        player['average'] = 0
        return str(player['average'])'''