import os
import sys

from dotenv import load_dotenv, dotenv_values

from controllers.GameFileHandler import GameFileHandler
from controllers.GamePersistenceFactory import GamePersistenceFactory
from controllers.GameSQLiteHandler import GameSQLiteHandler
from controllers.GameMySQLHandler import GameMySQLHandler
from models.Computer import Computer
from models.User import User
from views.Window import Window
from datetime import datetime


class Controller:
    def __init__(self):
        self.user = User()
        self.computer = Computer()
        self.window = Window(self)

    def show_user_frame(self):
        self.window.user_frame.tkraise()

    def show_game_frame(self, **kwargs):
        if 'username' in kwargs:
            username = kwargs.get('username')
            self.user.set_name(username)
            handler = GamePersistenceFactory.get_handler()
            self.user.history = handler.load_history(username)
            print(self.user.history)
        self.window.game_frame.tkraise()

    def show_score_frame(self, user_selection):
        print("User selected:" + user_selection)
        self.user.selection = user_selection
        self.computer.play_random()
        if self.user.selection == 'R' and self.computer.selection == 'S':
            self.user.add_win()
        elif self.user.selection == 'R' and self.computer.selection == 'P':
            self.computer.add_win()
        elif self.user.selection == 'P' and self.computer.selection == 'R':
            self.user.add_win()
        elif self.user.selection == 'P' and self.computer.selection == 'S':
            self.computer.add_win()
        elif self.user.selection == 'S' and self.computer.selection == 'P':
            self.user.add_win()
        elif self.user.selection == 'S' and self.computer.selection == 'R':
            self.computer.add_win()
        self.window.score_frame.tkraise()
        self.window.score_frame.update_score_label(self.user.score, self.computer.score)

    def close_app(self):
        handler = GamePersistenceFactory.get_handler()
        handler.save_game(self)
        # GameFileHandler.save_game(self)
        # GameSQLiteHandler.save_game(self)
        self.window.destroy()


