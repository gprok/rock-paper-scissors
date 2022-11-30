from controllers.GamePersistenceHandler import GamePersistenceHandler


class GameAPIHandler(GamePersistenceHandler):
    @staticmethod
    def save_game(controller):
        print("Sending to API")

    @staticmethod
    def load_history(username):
        print("Retrieving from API")

