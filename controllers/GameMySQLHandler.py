from controllers.GamePersistenceHandler import GamePersistenceHandler


class GameMySQLHandler(GamePersistenceHandler):
    @staticmethod
    def save_game(controller):
        print("Saving to MySQL")

    @staticmethod
    def load_history(username):
        print("retrieving from MySQL new version")