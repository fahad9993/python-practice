from tkinter import *

window = Tk()
window.minsize(width=500, height=300)
window.title("My first GUI Program")

my_label = Label(text="This is my label", font=("Arial", 10, "bold"))
my_label.pack()


# Button
def button_clicked():
    my_label.config(text=user_input.get())


button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
user_input = Entry(width=10)
user_input.pack()

window.mainloop()
