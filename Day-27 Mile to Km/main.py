from tkinter import *

window = Tk()
window.minsize(width=400, height=50)
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

# Configure the grid to have 3 columns with equal weight
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

mile = Entry(width=7)
mile.focus()
mile.grid(column=1, row=0)


def mile_to_km():
    km = float(mile.get()) * 1.6
    km_txt.config(text=km)


txt1 = Label(text="MIles")
txt1.grid(column=2, row=0)

txt2 = Label(text="is equal to")
txt2.grid(column=0, row=1)

km_txt = Label(text=0)
km_txt.grid(column=1, row=1)

txt3 = Label(text="Km")
txt3.grid(column=2, row=1)

button = Button()
button.config(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)

window.mainloop()
