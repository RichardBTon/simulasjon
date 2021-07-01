from random import random

# Probability that the players will win a serve
prob_1 = 0.65
prob_2 = 0.6

class Player:
    def __init__(self, prob):
        self.points = 0
        self.prob = prob
        self.serve = False
        self.games_won = 0

    def serve_sim(self):
        if random() < self.prob:
            self.points += 1
        else:
            self.serve = False

def sim_round(p1, p2):
    p1.serve = True

    while p1.points < 15 and p2.points < 15:
        # Veldig klønete, men orker ikke lage liste:
        if p1.serve:
            p1.serve_sim()
            if not p1.serve:
                p2.serve = True
        elif p2.serve:
            p2.serve_sim()
            if not p2.serve:
                p1.serve = True
        else:
            print("Det er ingen som server. Noe gikk galt")
            break
    
    else:
        # Samme her:
        if p1.points > 14:
            return p1
        if p2.points > 14:
            return p2

player_1 = Player(prob_1)
player_2 = Player(prob_2)

num_of_games = 10000

for round in range(num_of_games):
    player_1.points = 0
    player_2.points = 0

    winner = sim_round(player_1, player_2)
    winner.games_won += 1

print(f'''
Player 1 won {player_1.games_won} games. That is {player_1.games_won/num_of_games * 100}%.
Player 2 won {player_2.games_won} games. That is {player_2.games_won/num_of_games * 100}%.
''')









