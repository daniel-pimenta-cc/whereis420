from http import client
from fastapi import FastAPI, Request
from datetime import datetime
import pytz
app = FastAPI()


@app.get("/")
async def root(request: Request):

    timezones = [
        {'city': 'Pago Pago', 'country': 'American Samoa','timezone': 'Pacific/Pago_Pago'},
        {'city': 'Honolulu', 'country': 'USA','timezone': 'Pacific/Honolulu'},
        {'city': 'Rikitea', 'country': 'French Polynesia','timezone': 'Pacific/Gambier'},
        {'city': 'Anchorage', 'country': 'USA','timezone': 'America/Anchorage'},
        {'city': 'Los Angeles', 'country': 'USA','timezone': 'America/Los_Angeles'},
        {'city': 'San José', 'country': 'USA','timezone': 'America/Costa_Rica'},
        {'city': 'Mexico City', 'country': 'Mexico','timezone': 'America/Mexico_City'},
        {'city': 'New York', 'country': 'USA','timezone': 'America/New_York'},
        {'city': 'São Paulo', 'country': 'Brazil','timezone': 'America/Sao_Paulo'},
        {'city': 'St John\'s', 'country': 'Canada','timezone': 'America/St_Johns'},
        {'city': 'Fernando de Noronha', 'country': 'Brazil','timezone': 'America/Noronha'},
        {'city': 'Praia', 'country': 'Cabo Verde','timezone': 'Atlantic/Cape_Verde'},
        {'city': 'Accra', 'country': 'Ghana','timezone': 'Africa/Accra'},
        {'city': 'London', 'country': 'UK','timezone': 'Europe/London'},
        {'city': 'Cairo', 'country': 'Egypt','timezone': 'Africa/Cairo'},
        {'city': 'Moscow', 'country': 'Russia','timezone': 'Europe/Moscow'},
        {'city': 'Baku', 'country': 'Azerbaijan','timezone': 'Asia/Baku'},
        {'city': 'Tehran', 'country': 'Iran','timezone': 'Asia/Tehran'},
        {'city': 'Karachi', 'country': 'Pakistan','timezone': 'Asia/Karachi'},
        {'city': 'Mumbai', 'country': 'India','timezone': 'Asia/Kolkata'},
        {'city': 'Kathmandu', 'country': 'Nepal','timezone': 'Asia/Kathmandu'},
        {'city': 'Daka', 'country': 'Bangladesh','timezone': 'Asia/Dhaka'},
        {'city': 'Yangon', 'country': 'Myanmar','timezone': 'Asia/Yangon'},
        {'city': 'Jakarta', 'country': 'Indonesia','timezone': 'Asia/Jakarta'},
        {'city': 'Shanghai', 'country': 'China','timezone': 'Asia/Shanghai'},
        {'city': 'Tokyo', 'country': 'Japan','timezone': 'Asia/Tokyo'},
        {'city': 'Brisbane', 'country': 'Australia','timezone': 'Australia/Brisbane'},
        {'city': 'Port Vila', 'country': 'Vanuatu','timezone': 'Pacific/Efate'},
        {'city': 'Auckland', 'country': 'New Zealand','timezone': 'Pacific/Auckland'},
    ]

    for i in timezones:
        local_time = datetime.now(pytz.timezone(i['timezone']))
        four_20_pm = local_time.replace(hour=16, minute=20, second=0, microsecond=0)
        four_30_pm = local_time.replace(hour=16, minute=30, second=0, microsecond=0)
        three_30_pm =  local_time.replace(hour=15, minute=30, second=0, microsecond=0)
        if local_time > four_20_pm and local_time < four_30_pm:
            print(f' Is 4:{local_time.minute} in {i["city"]}, {i["country"]}')
        elif local_time < four_20_pm and local_time > three_30_pm:
            if local_time.hour == 15:
                minutes_to_420 = (60 - local_time.minute) + 20
            else:
                minutes_to_420 = 20 - local_time.minute
            print(f' It will be 4:20 in {i["city"]}, {i["country"]} in {minutes_to_420} minutes')
            

        


