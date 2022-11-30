from tkinter import Tk, Frame

from views.GameFrame import GameFrame
from views.ScoreFrame import ScoreFrame
from views.UserFrame import UserFrame


class Window(Tk):

    def __init__(self, controller):
        super(Window, self).__init__()
        self.geometry("400x200")

        self.controller = controller

        # container will act as the Stage
        # sub-frames (scenes) will be presented here
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.user_frame = UserFrame(container, self.controller)
        self.user_frame.grid(row=0, column=0, sticky="nsew")

        self.game_frame = GameFrame(container, self.controller)
        self.game_frame.grid(row=0, column=0, sticky="nsew")

        self.score_frame = ScoreFrame(container, self.controller)
        self.score_frame.grid(row=0, column=0, sticky="nsew")

        self.user_frame.tkraise()

