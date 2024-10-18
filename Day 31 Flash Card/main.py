from tkinter import *
import pandas
import random
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    if len(to_learn) > 0:
        current_card = random.choice(to_learn)
    else:
        start_over()
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


def is_known():
    if len(to_learn) > 0:
        to_learn.remove(current_card)
        data = pandas.DataFrame(to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
        next_card()
    else:
        start_over()


def start_over():
    global to_learn
    start_again = messagebox.askyesno(title="Empty list!", message="No words to learn. Do you want to start over?")
    if start_again:
        original_data = pandas.read_csv("data/french_words.csv")
        to_learn = original_data.to_dict(orient="records")


# ------------------- UI SETUP -------------------- #

window = Tk()
window.title("Flushy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, font=("Arial", 24, "italic"))
card_word = canvas.create_text(400, 263, font=("Arial", 36, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
unknown_button_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

known_button_img = PhotoImage(file="images/right.png")
known_button = Button(image=known_button_img, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
