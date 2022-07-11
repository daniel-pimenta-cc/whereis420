from http import client
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
import pytz
templates = Jinja2Templates(directory="templates/")


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root(request: Request):
    
    #get timezone of the request
    client_ip = pytz.timezone(request.headers.get("Timezone", "UTC"))
    client_host = request.client.host

    timezones = [
        {'city': 'Pago Pago','population':12576, 'country': 'American Samoa','timezone': 'Pacific/Pago_Pago', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_American_Samoa_-_Circle-256.png'},
        {'city': 'Honolulu','population':820987, 'country': 'USA','timezone': 'Pacific/Honolulu', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_the_United_States_-_Circle-256.png'},
        {'city': 'Rikitea','population':1200, 'country': 'French Polynesia','timezone': 'Pacific/Gambier', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_French_Polynesia_-_Circle-256.png'},
        {'city': 'Anchorage','population': 247949, 'country': 'USA','timezone': 'America/Anchorage', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_the_United_States_-_Circle-256.png'},
        {'city': 'Los Angeles',"population": 12750807, 'country': 'USA','timezone': 'America/Los_Angeles', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_the_United_States_-_Circle-256.png'},
        {'city': 'San José',"population": 1798103, 'country': 'USA','timezone': 'America/Costa_Rica', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_the_United_States_-_Circle-256.png'},
        {'city': 'Mexico City',"population": 20996000, 'country': 'Mexico','timezone': 'America/Mexico_City', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_Mexico_-_Circle-256.png'},
        {'city': 'New York',"population": 18713220, 'country': 'USA','timezone': 'America/New_York', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_the_United_States_-_Circle-256.png'},
        {'city': 'São Paulo',"population": 22046000, 'country': 'Brazil','timezone': 'America/Sao_Paulo', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_Brazil_-_Circle-256.png'},
        {'city': 'St John\'s',"population": 111914, 'country': 'Canada','timezone': 'America/St_Johns', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_Canada_-_Circle-256.png'},
        {'city': 'Fernando de Noronha',"population": 3101, 'country': 'Brazil','timezone': 'America/Noronha', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_Brazil_-_Circle-256.png'},
        {'city': 'Praia',"population": 127832, 'country': 'Cape Verde','timezone': 'Atlantic/Cape_Verde', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_Cape_Verde_-_Circle-256.png'},
        {'city': 'Accra',"population": 2291352, 'country': 'Ghana','timezone': 'Africa/Accra', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_Ghana_-_Circle-256.png'},
        {'city': 'London',"population": 10979000, 'country': 'UK','timezone': 'Europe/London', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_the_United_Kingdom_-_Circle-256.png'},
        {'city': 'Cairo',"population": 19372000, 'country': 'Egypt','timezone': 'Africa/Cairo', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_Egypt_-_Circle-256.png'},
        {'city': 'Moscow',"population": 17125000, 'country': 'Russia','timezone': 'Europe/Moscow', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_Russia_-_Circle-256.png'},
        {'city': 'Baku',"population": 2181800, 'country': 'Azerbaijan','timezone': 'Asia/Baku', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_Azerbaijan_-_Circle-256.png'},
        {'city': 'Tehran',"population": 13633000, 'country': 'Iran','timezone': 'Asia/Tehran', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_Iran_-_Circle-256.png'},
        {'city': 'Karachi',"population": 14835000, 'country': 'Pakistan','timezone': 'Asia/Karachi', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_Pakistan_-_Circle-256.png'},
        {'city': 'Mumbai',"population": 23355000, 'country': 'India','timezone': 'Asia/Kolkata', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_India_-_Circle-256.png'},
        {'city': 'Kathmandu',"population": 975453, 'country': 'Nepal','timezone': 'Asia/Kathmandu', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_Nepal_-_Circle-256.png'},
        {'city': 'Daka',"population": 1146053, 'country': 'Bangladesh','timezone': 'Asia/Dhaka', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_Bangladesh_-_Circle-256.png'},
        {'city': 'Yangon',"population": 5514000, 'country': 'Myanmar','timezone': 'Asia/Yangon', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_Myanmar_-_Circle-256.png'},
        {'city': 'Jakarta',"population": 34540000, 'country': 'Indonesia','timezone': 'Asia/Jakarta', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_Indonesia_-_Circle-256.png'},
        {'city': 'Shanghai',"population": 22120000, 'country': 'China','timezone': 'Asia/Shanghai', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_China_-_Circle-256.png'},
        {'city': 'Tokyo',"population": 37977000, 'country': 'Japan','timezone': 'Asia/Tokyo', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_Japan_-_Circle-256.png'},
        {'city': 'Brisbane', "population": 2514184, 'country': 'Australia','timezone': 'Australia/Brisbane', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_Australia_-_Circle-256.png'},
        {'city': 'Port Vila', "population": 51437, 'country': 'Vanuatu','timezone': 'Pacific/Efate', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_Vanuatu_-_Circle-256.png'},
        {'city': 'Auckland',"population": 1467800,  'country': 'New Zealand','timezone': 'Pacific/Auckland', 'flag':'https://cdn4.iconfinder.com/data/icons/world-flags-circular/1000/Flag_of_New_Zealand_-_Circle-256.png'},
    ]

    print(client_host)
    
    for i in range(len(timezones)):
        local_time = datetime.now(pytz.timezone(timezones[i]['timezone']))
        four_20_pm = local_time.replace(hour=16, minute=20, second=0, microsecond=0)
        four_30_pm = local_time.replace(hour=16, minute=30, second=0, microsecond=0)
        three_30_pm =  local_time.replace(hour=15, minute=30, second=0, microsecond=0)
        
        if local_time > four_20_pm and local_time < four_30_pm:
            return templates.TemplateResponse("index.html", {"request": request, 'text': f'Is 4:{local_time.minute} in {timezones[i]["city"]}, {timezones[i]["country"]}', 'index': str(i)})
            #return(f'Is 4:{local_time.minute} in {i["city"]}, {i["country"]}')
        elif local_time < four_20_pm and local_time > three_30_pm:
            if local_time.hour == 15:
                minutes_to_420 = (60 - local_time.minute) + 20
            else:
                minutes_to_420 = 20 - local_time.minute
            return templates.TemplateResponse("index.html", {"request": request, 'text': f'It will be 4:20 in {timezones[i]["city"]}, {timezones[i]["country"]} in {minutes_to_420} minutes', 'index': str(i)})
            #return(f'It will be 4:20 in {i["city"]}, {i["country"]} in {minutes_to_420} minutes')
            

        
