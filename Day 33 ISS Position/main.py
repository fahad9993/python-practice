import requests
from datetime import datetime

MY_LAT = 23.810331  # Your latitude
MY_LONG = 90.412521  # Your longitude

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
