from tkinter import Frame, Label, Button


class GameFrame(Frame):

    def __init__(self, parent, controller):
        super(GameFrame, self).__init__(parent)
        self.controller = controller
        label = Label(self, text="PLAY")
        # label.pack(side="top", fill="x", pady=10)
        label.grid(row=0, column=0, columnspan=3)

        rock_btn = Button(self, text="R",
                           command=lambda: controller.show_score_frame("R"))
        rock_btn.grid(row=1, column=0)
        paper_btn = Button(self, text="P",
                          command=lambda: controller.show_score_frame("P"))
        paper_btn.grid(row=1, column=1)
        scissors_btn = Button(self, text="S",
                          command=lambda: controller.show_score_frame("S"))
        scissors_btn.grid(row=1, column=2)
