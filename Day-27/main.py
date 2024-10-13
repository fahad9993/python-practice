from tkinter import *

window = Tk()
window.minsize(width=500, height=300)
window.title("My first GUI Program")

my_label = Label(text="This is my label", font=("Arial", 10, "bold"))
my_label.grid(column=0, row=0)


# Button
def button_clicked():
    my_label.config(text=user_input.get())


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click again")
new_button.grid(column=2, row=0)

# Entry
user_input = Entry(width=10)
user_input.grid(column=3, row=2)

window.mainloop()
