from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])


# ------------------- UI SETUP -------------------- #

window = Tk()
window.title("Flushy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 24, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 36, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
unknown_button_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

known_button_img = PhotoImage(file="images/right.png")
known_button = Button(image=known_button_img, highlightthickness=0, command=next_card)
known_button.grid(column=1, row=1)

window.mainloop()
