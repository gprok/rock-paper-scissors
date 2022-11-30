
class Player:
    options = ['R', 'P', 'S']

    def __init__(self):
        self.selection = None
        self.score = 0

    def add_win(self):
        self.score += 1


