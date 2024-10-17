from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ------------------- UI SETUP -------------------- #

window = Tk()
window.title("Flushy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Arial", 24, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 36, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
unknown_button_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_img, highlightthickness=0)
unknown_button.grid(column=0, row=1)

known_button_img = PhotoImage(file="images/right.png")
known_button = Button(image=known_button_img, highlightthickness=0)
known_button.grid(column=1, row=1)

window.mainloop()
