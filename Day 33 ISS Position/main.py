import requests
from datetime import datetime
import os
from dotenv import load_dotenv
import smtplib

MY_LAT = 23.810331  # Your latitude
MY_LONG = 90.412521  # Your longitude

load_dotenv()
SMTP_SERVER = "smtp.gmail.com"
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "time_format": 24,
}


def is_iss_overhead():
    res = requests.get(url="http://api.open-notify.org/iss-now.json")
    res.raise_for_status()

    iss_data = res.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    print(iss_longitude, iss_latitude)

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    response = requests.get(url="https://api.sunrisesunset.io/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split(":")[0])
    sunset = int(data["results"]["sunset"].split(":")[0])
    print(f"sunrise: {sunrise}\nsunset:{sunset}")
    now = datetime.now().hour

    if sunset <= now or now <= sunrise:
        return True


if is_iss_overhead() and is_night():
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg="Subject:ISS is overhead!\n\nHey, Look out! The ISS is over your city. You can look for it in the sky."
        )
