import os

from dotenv import load_dotenv

from controllers.GameAPIHandler import GameAPIHandler
from controllers.GameFileHandler import GameFileHandler
from controllers.GameMySQLHandler import GameMySQLHandler
from controllers.GameSQLiteHandler import GameSQLiteHandler


class GamePersistenceFactory:
    @staticmethod
    def get_handler():
        load_dotenv()
        type = os.environ.get("GAME_HANDLER")
        if type == 'file':
            return GameFileHandler()
        elif type == 'sqlite':
            return GameSQLiteHandler()
        elif type == 'mysql':
            return GameMySQLHandler()
        elif type == 'api':
            return GameAPIHandler()

