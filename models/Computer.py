import random

from models.Player import Player


class Computer(Player):
    def __init__(self):
        super(Computer, self).__init__()

    def __str__(self):
        return "computer"

    def play_random(self):
        rnd = random.randint(0, 2)
        self.selection = Player.options[rnd]
        print("Computer selected: " + self.selection)

