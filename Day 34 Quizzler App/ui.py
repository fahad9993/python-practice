from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: 0", font=12)
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Question text", font=FONT, fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right_button_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_button_img, highlightthickness=0)
        self.right_button.grid(column=0, row=2)

        wrong_button_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_button_img, highlightthickness=0)
        self.wrong_button.grid(column=1, row=2)

        self.window.mainloop()
