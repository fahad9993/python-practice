import requests

API_KEY = "c0134beaf9bf362e6a4a4f02064460f3"
MY_LAT = 23.810331
My_LONG = 90.412521

# https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
parameters = {
    "lat": MY_LAT,
    "lon": My_LONG,
    "appid": API_KEY,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()


def will_rain():
    hour = 0
    for _ in range(1, 11):
        weather_id = response.json()["list"][hour]["weather"][0]["id"]
        hour += 1
        if weather_id < 700:
            return True


if will_rain():
    print("Bring and umbrella.")
