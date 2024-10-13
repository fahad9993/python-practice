from tkinter import *

window = Tk()
window.minsize(width=500, height=300)

my_label = Label(text="This is my label", font=("Arial", 10, "bold"))
my_label.pack()


# Button
def button_clicked():
    if my_label["text"] == "This is my label":
        my_label.config(text="Button got clicked")
    else:
        my_label.config(text="This is my label")


button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
user_input = Entry(width=10)
user_input.pack()



window.mainloop()
