import csv
from datetime import datetime

from controllers.GamePersistenceHandler import GamePersistenceHandler


class GameFileHandler(GamePersistenceHandler):
    @staticmethod
    def save_game(controller):
        file = open("data/score.csv", "a")
        file.write(controller.user.name + ',' + str(datetime.now()) + ',' +
                   str(controller.user.score) + ',' + str(controller.computer.score) + '\n')
        file.close()

    @staticmethod
    def load_history(username):
        history = []
        with open('data/score.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username:
                    history.append(row)
        return history
