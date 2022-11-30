from tkinter import Frame, Label, Button, Text, END


class UserFrame(Frame):

    def __init__(self, parent, controller):
        super(UserFrame, self).__init__(parent)
        self.controller = controller

        label = Label(self, text="Username: ")
        #label.pack(side="top", fill="x", pady=10)
        label.grid(row=0, column=0)
        self.user_field = Text(self, height = 2, width = 30)
        #user_field.pack(side="top", fill="x", pady=10)
        self.user_field.grid(row=0, column=1)

        play_btn = Button(self, text="PLAY",
                            command=self.submit)
        button2 = Button(self, text="Go to Page Two",
                         command=lambda: controller.show_frame(controller.score_frame))
        # button1.pack()
        # button2.pack()
        play_btn.grid(row=1, column=0)

        self.error_label = Label(self, text="")
        # label.pack(side="top", fill="x", pady=10)
        self.error_label.grid(row=2, column=0, columnspan=2)

    def submit(self):
        username = self.user_field.get("1.0", END).strip()
        if len(username) == 0:
            self.error_label.config(text="Error: Username cannot be empty")
        else:
            self.controller.show_game_frame(username=username)
