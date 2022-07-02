from datetime import datetime
from threading import local
import pytz

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
        
       

def whereis420(timezones, now_gmt):
    if now_gmt.hour == 0 and now_gmt.minute < 30:
        return {
        'city' : timezones[3]['city'],
        'country' : timezones[3]['country']
    }
    elif now_gmt.hour == 1 and now_gmt.minute < 30:
        return {
        'city' : timezones[3]['city'],
        'country' : timezones[3]['country']
    }
    elif now_gmt.hour == 2 and now_gmt.minute < 30:
        return {
        'city' : timezones[2]['city'],
        'country' : timezones[2]['country']
    }
    elif now_gmt.hour == 3 and now_gmt.minute < 30:
        return {
        'city' : timezones[1]['city'],
        'country' : timezones[1]['country']
    }
    elif now_gmt.hour == 4 and now_gmt.minute < 30:
        return {
        'city' : timezones[0]['city'],
        'country' : timezones[0]['country']
    }
    elif now_gmt.hour == 5 and now_gmt.minute < 30:
        return {
        'city' : timezones[27]['city'],
        'country' : timezones[27]['country']
    }
    elif now_gmt.hour == 6 and now_gmt.minute < 30:
        return {
        'city' : timezones[26]['city'],
        'country' : timezones[26]['country']
    }
    elif now_gmt.hour == 7 and now_gmt.minute < 30:
        return {
        'city' : timezones[25]['city'],
        'country' : timezones[25]['country']
    }
    elif now_gmt.hour == 8 and now_gmt.minute < 30:
        return {
        'city' : timezones[24]['city'],
        'country' : timezones[24]['country']
    }
    elif now_gmt.hour == 9 and now_gmt.minute < 30:
        return {
        'city' : timezones[23]['city'],
        'country' : timezones[23]['country']
    }
    elif now_gmt.hour == 9 and now_gmt.minute > 30:
        return {
        'city' : timezones[22]['city'],
        'country' : timezones[22]['country']
    }
    elif now_gmt.hour == 10 and now_gmt.minute < 30:                  
        return {
        'city' : timezones[21]['city'],
        'country' : timezones[21]['country']
    }
    elif now_gmt.hour == 10 and now_gmt.minute > 30:
        return {
        'city' : timezones[20]['city'],
        'country' : timezones[20]['country']
    }
    elif now_gmt.hour == 10 and now_gmt.minute < 59:
        return {
        'city' : timezones[19]['city'],
        'country' : timezones[19]['country']
    }
    elif now_gmt.hour == 11 and now_gmt.minute < 30:
        return {
        'city' : timezones[18]['city'],
        'country' : timezones[18]['country']
    }
    elif now_gmt.hour == 11 and now_gmt.minute > 30:
        return {
        'city' : timezones[17]['city'],
        'country' : timezones[17]['country']
    }
    elif now_gmt.hour == 12 and now_gmt.minute < 30:
        return {
        'city' : timezones[16]['city'],
        'country' : timezones[16]['country']
    }
    elif now_gmt.hour == 13 and now_gmt.minute < 30:
        return {
        'city' : timezones[15]['city'],
        'country' : timezones[15]['country']
    }
    elif now_gmt.hour == 14 and now_gmt.minute < 30:
        return {
        'city' : timezones[14]['city'],
        'country' : timezones[14]['country']
    }
    elif now_gmt.hour == 15 and now_gmt.minute < 30:
        return {
        'city' : timezones[13]['city'],
        'country' : timezones[13]['country']
    }
    elif now_gmt.hour == 16 and now_gmt.minute < 30:
        return {
        'city' : timezones[12]['city'],
        'country' : timezones[12]['country']
    }
    elif now_gmt.hour == 17 and now_gmt.minute < 30:
        return {
        'city' : timezones[11]['city'],
        'country' : timezones[11]['country']
    }
    elif now_gmt.hour == 18 and now_gmt.minute < 30:
        return {
        'city' : timezones[10]['city'],
        'country' : timezones[10]['country']
    }
    elif now_gmt.hour == 19 and now_gmt.minute < 30:
        return {
        'city' : timezones[9]['city'],
        'country' : timezones[9]['country']
    }
    elif now_gmt.hour == 20 and now_gmt.minute > 30:
        return {
        'city' : timezones[8]['city'],
        'country' : timezones[8]['country']
    }
    elif now_gmt.hour == 21 and now_gmt.minute < 30:
        return {
        'city' : timezones[7]['city'],
        'country' : timezones[7]['country']
    }
    elif now_gmt.hour == 22 and now_gmt.minute < 30:
        return {
        'city' : timezones[6]['city'],
        'country' : timezones[6]['country']
    }
    elif now_gmt.hour == 23 and now_gmt.minute < 30:
        return {
        'city' : timezones[5]['city'],
        'country' : timezones[5]['country']
    }
    elif now_gmt.hour == 23 and now_gmt.minute > 30:
        return {
        'city' : timezones[4]['city'],
        'country' : timezones[4]['country']
    }

