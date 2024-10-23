import requests
from datetime import datetime

MY_LAT = 23.810331  # Your latitude
MY_LONG = 90.412521  # Your longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "time_format": 24,
}
response = requests.get(url="https://api.sunrisesunset.io/json", params=parameters)
response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split(":")[0])
    sunset = int(data["results"]["sunset"].split(":")[0])
    print(f"sunrise: {sunrise}\nsunset:{sunset}")
    now = datetime.now().hour

    if sunset <= now or now <= sunrise:
        return True
