import datetime as dt
import smtplib
import os
from dotenv import load_dotenv
import pandas
import random

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

now = dt.datetime.now()
day_today = now.day
month_today = now.month

data = pandas.read_csv("birthdays.csv")

for (index, row) in data.iterrows():
    letter_no = random.randint(1, 3)
    print(letter_no)
    if row.month == month_today and row.day == day_today:
        with open(f"letter_templates/letter_{letter_no}.txt") as letter_file:
            letter = letter_file.read().replace("[NAME]", row.f_name)

        with smtplib.SMTP(SMTP_SERVER) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=row.email,
                                msg=f"Subject: Happy Birthday {row.f_name}!\n\n{letter}"
                                )
