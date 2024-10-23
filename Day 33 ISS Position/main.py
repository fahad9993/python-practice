import requests
MY_LAT = 23.810331
MY_LONG = 90.412521

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}
response = requests.get(url="https://api.sunrisesunset.io/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise, sunset)