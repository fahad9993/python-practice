import tkinter as tk
from tkcalendar import DateEntry
from datetime import datetime, timedelta

class StreakCounterApp:
    def __init__(self, master):
        self.master = master
        master.title("Streak Counter")

        self.datetime_label = tk.Label(master, text="Start Date and Time:", font=("Helvetica", 12))
        self.datetime_label.pack()

        # Date Entry widget for selecting the start date
        self.date_entry = DateEntry(master, width=12, background='lightgray',
                                     foreground='black', borderwidth=2, font=("Arial", 10))
        self.date_entry.pack(pady=10)

        # Time Entry widget for selecting the start time
        self.time_entry = tk.Entry(master, bg="lightgray", fg="black", font=("Arial", 10))
        self.time_entry.insert(0, "00:00:00")
        self.time_entry.pack()

        self.start_button = tk.Button(master, text="Start Streak", command=self.start_streak,
                                      bg="green", fg="white", font=("Arial", 12), padx=10, pady=5)
        self.start_button.pack()

        self.reset_button = tk.Button(master, text="Reset Streak", command=self.reset_streak,
                                      bg="red", fg="white", font=("Arial", 12), padx=10, pady=5)
        self.reset_button.pack()

        self.streak_label = tk.Label(master, text="Streak: 0 days", font=("Helvetica", 14))
        self.streak_label.pack()

        self.streak = 0
        self.start_date = None

    def start_streak(self):
        selected_date = self.date_entry.get_date()
        selected_time = self.time_entry.get()
        selected_datetime_str = f"{selected_date} {selected_time}"

        # Convert the selected datetime string to a datetime object
        self.start_date = datetime.strptime(selected_datetime_str, '%Y-%m-%d %H:%M:%S').date()

        # Calculate the streak
        today = datetime.now().date()
        if today - self.start_date == timedelta(days=self.streak):
            self.streak += 1
        else:
            self.streak = (today - self.start_date).days
        self.update_streak_label()

    def reset_streak(self):
        self.streak = 0
        self.update_streak_label()

    def update_streak_label(self):
        self.streak_label.config(text=f"Streak: {self.streak} days")

root = tk.Tk()
app = StreakCounterApp(root)
root.mainloop()
