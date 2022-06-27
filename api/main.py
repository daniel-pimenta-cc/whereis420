from http import client
from fastapi import FastAPI, Request
from datetime import datetime
import pytz
app = FastAPI()


@app.get("/")
async def root(request: Request):

    timezones = [
        {'city': 'Pago Pago', 'country': 'American Samoa'},
        {'city': 'Honolulu', 'country': 'USA'},
        {'city': 'Rikitea', 'country': 'French Polynesia'},
        {'city': 'Anchorage', 'country': 'USA'},
        {'city': 'Los Angeles', 'country': 'USA'},
        {'city': 'San José', 'country': 'USA'},
        {'city': 'Mexico City', 'country': 'Mexico'},
        {'city': 'New York', 'country': 'USA'},
        {'city': 'São Paulo', 'country': 'Brazil'},
        {'city': 'St John\'s', 'country': 'Canada'},
        {'city': 'Fernando de Noronha', 'country': 'Brazil'},
        {'city': 'Praia', 'country': 'Cabo Verde'},
        {'city': 'Accra', 'country': 'Ghana'},
        {'city': 'London', 'country': 'UK'},
        {'city': 'Cairo', 'country': 'Egypt'},
        {'city': 'Moscow', 'country': 'Russia'},
        {'city': 'Baku', 'country': 'Azerbaijan'},
        {'city': 'Tehran', 'country': 'Iran'},
        {'city': 'Karachi', 'country': 'Pakistan'},
        {'city': 'Mumbai', 'country': 'India'},
        {'city': 'Kathmandu', 'country': 'Nepal'},
        {'city': 'Daka', 'country': 'Bangladesh'},
        {'city': 'Yangon', 'country': 'Myanmar'},
        {'city': 'Jakarta', 'country': 'Indonesia'},
        {'city': 'Shanghai', 'country': 'China'},
        {'city': 'Tokyo', 'country': 'Japan'},
        {'city': 'Brisbane', 'country': 'Australia'},
        {'city': 'Port Vila', 'country': 'Vanuatu'},
        {'city': 'Auckland', 'country': 'New Zealand'},
    ]

    now_gmt = datetime.now(pytz.timezone('Africa/Accra'))
    print(now_gmt.hour)
    print(now_gmt.minute)

    if now_gmt.hour == 0 and now_gmt.minute < 30:
        return(timezones[3]['city'] + " " + timezones[3]['country'])
    elif now_gmt.hour == 1 and now_gmt.minute < 30:
        return(timezones[3]['city'] + " " + timezones[3]['country'])
    elif now_gmt.hour == 2 and now_gmt.minute < 30:
        return(timezones[2]['city'] + " " + timezones[2]['country'])
    elif now_gmt.hour == 3 and now_gmt.minute < 30:
        return(timezones[1]['city'] + " " + timezones[1]['country'])
    elif now_gmt.hour == 4 and now_gmt.minute < 30:
        return(timezones[0]['city'] + " " + timezones[0]['country'])
    elif now_gmt.hour == 5 and now_gmt.minute < 30:
        return(timezones[27]['city'] + " " + timezones[27]['country'])
    elif now_gmt.hour == 6 and now_gmt.minute < 30:
        return(timezones[26]['city'] + " " + timezones[26]['country'])
    elif now_gmt.hour == 7 and now_gmt.minute < 30:
        return(timezones[25]['city'] + " " + timezones[25]['country']) 
    elif now_gmt.hour == 8 and now_gmt.minute < 30:
        return(timezones[24]['city'] + " " + timezones[24]['country']) 
    elif now_gmt.hour == 9 and now_gmt.minute < 30:
        return(timezones[23]['city'] + " " + timezones[23]['country']) 
    elif now_gmt.hour == 9 and now_gmt.minute > 30:
        return(timezones[22]['city'] + " " + timezones[22]['country'])
    elif now_gmt.hour == 10 and now_gmt.minute < 30:                  
        return(timezones[21]['city'] + " " + timezones[21]['country'])
    elif now_gmt.hour == 10 and now_gmt.minute > 30:
        return(timezones[20]['city'] + " " + timezones[20]['country'])
    elif now_gmt.hour == 10 and now_gmt.minute < 59:
        return(timezones[19]['city'] + " " + timezones[19]['country']) 
    elif now_gmt.hour == 11 and now_gmt.minute < 30:
        return(timezones[18]['city'] + " " + timezones[18]['country'])
    elif now_gmt.hour == 11 and now_gmt.minute > 30:
        return(timezones[17]['city'] + " " + timezones[17]['country'])
    elif now_gmt.hour == 12 and now_gmt.minute < 30:
        return(timezones[16]['city'] + " " + timezones[16]['country']) #
    elif now_gmt.hour == 13 and now_gmt.minute < 30:
        return(timezones[15]['city'] + " " + timezones[15]['country'])
    elif now_gmt.hour == 14 and now_gmt.minute < 30:
        return(timezones[14]['city'] + " " + timezones[14]['country'])
    elif now_gmt.hour == 15 and now_gmt.minute < 30:
        return(timezones[13]['city'] + " " + timezones[13]['country'])
    elif now_gmt.hour == 16 and now_gmt.minute < 30:
        return(timezones[12]['city'] + " " + timezones[12]['country'])
    elif now_gmt.hour == 17 and now_gmt.minute < 30:
        return(timezones[11]['city'] + " " + timezones[11]['country'])
    elif now_gmt.hour == 18 and now_gmt.minute < 30:
        return(timezones[10]['city'] + " " + timezones[10]['country'])
    elif now_gmt.hour == 19 and now_gmt.minute < 30:
        return(timezones[9]['city'] + " " + timezones[9]['country'])
    elif now_gmt.hour == 20 and now_gmt.minute > 30:
        return(timezones[8]['city'] + " " + timezones[8]['country'])
    elif now_gmt.hour == 21 and now_gmt.minute < 30:
        return(timezones[7]['city'] + " " + timezones[7]['country'])
    elif now_gmt.hour == 22 and now_gmt.minute < 30:
        return(timezones[6]['city'] + " " + timezones[6]['country'])
    elif now_gmt.hour == 23 and now_gmt.minute < 30:
        return(timezones[5]['city'] + " " + timezones[5]['country'])
    elif now_gmt.hour == 23 and now_gmt.minute > 30:
        return(timezones[4]['city'] + " " + timezones[4]['country'])

    


