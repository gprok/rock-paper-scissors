from tkinter import Frame, Label, Button


class ScoreFrame(Frame):

    def __init__(self, parent, controller):
        super(ScoreFrame, self).__init__(parent)
        self.controller = controller
        self.score_label = Label(self, text="Score:")
        self.score_label.grid(row=0, column=0)
        play_again_btn = Button(self, text="Play again",
                                command=lambda: controller.show_game_frame())
        exit_btn = Button(self, text="EXIT",
                          command=lambda: controller.close_app())
        play_again_btn.grid(row=1, column=0)
        exit_btn.grid(row=2, column=0)

    def update_score_label(self, user_score, computer_score):
        self.score_label.config(text="Score: User-Computer " + str(user_score) + " - " + str(computer_score))

