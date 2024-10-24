import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_URL = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.getenv("STOCK_API_KEY"),
}

yesterday = f"{datetime.now().date()-timedelta(1)}"
the_day_before = f"{datetime.now().date()-timedelta(2)}"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url=STOCK_API_URL, params=stock_params)
response.raise_for_status()
data = response.json()
print(data)
yesterday_data = float(response.json()["Time Series (Daily)"][yesterday]["4. close"])
the_day_before_data = float(response.json()["Time Series (Daily)"][the_day_before]["4. close"])
print(yesterday_data)
print(the_day_before_data)
percent = (yesterday_data - the_day_before_data) / yesterday_data * 100
print(percent)
if percent >= 5 or percent <= -5:
    print("Get News")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
