from abc import ABC, abstractmethod


class GamePersistenceHandler(ABC):
    @staticmethod
    @abstractmethod
    def save_game(controller):
        pass

    @staticmethod
    @abstractmethod
    def load_history(username):
        pass
