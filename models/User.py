from models.Player import Player


class User(Player):
    def __init__(self):
        super(User, self).__init__()
        self.name = ''
        self.history = []

    def set_name(self, name: str):
        self.name = name

    def set_history(self, history: list):
        self.history = history

    def __str__(self):
        return self.name