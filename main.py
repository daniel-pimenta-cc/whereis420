from http import client
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime, timedelta
from data import timezones_data
import pytz
import json
templates = Jinja2Templates(directory="templates/")
from pytz import timezone
from heapq import nsmallest

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root(request: Request):
    #itera sobre os dados de cada timezone e retorna uma lista contendo só o nome das timezone
    timezones_names = [timezones_data[i]['timezone'] for i in range(len(timezones_data))]
    datetime_420 = datetime.now().replace(hour=16, minute=20, second=0, microsecond=0)
    datetime_420 = datetime_420.time()
    closest_tz = find_next_timezone(timezones_names)
    local_time = datetime.now(pytz.timezone(closest_tz))
    local_time = local_time.replace(microsecond=0)
    local_time = local_time.replace(second=0)
    local_time = local_time.time()
    i = timezones_names.index(closest_tz)
    minutes_to_420 = (datetime_420.hour - local_time.hour) * 60 + (datetime_420.minute - local_time.minute)
    is_420 = False
    if local_time >= datetime_420 and local_time <= datetime.strptime("16:30", "%H:%M").time():
        is_420 = True


    return templates.TemplateResponse("index.html", 
    {
        "request": request,
        'text': f'It will be 4:20 in {timezones_data[i]["city"]}, {timezones_data[i]["country"]} in {minutes_to_420} minutes',
        'map_img': timezones_data[i]['map'],
        'city': timezones_data[i]['city'],
        'country': timezones_data[i]['country'],
        'timezone': timezones_data[i]['timezone'],
        'desc': timezones_data[i]['desc'],
        'sub_desc': timezones_data[i]['subdesc'],
        'pop_count': timezones_data[i]['population'],
        'current_hour': local_time.hour,
        'current_minute': local_time.minute if local_time.minute >= 10 else f'0{local_time.minute}',
        'minutes_to_420': minutes_to_420,
        'is_420': is_420,
    })
        
@app.get("/next_city_data")
async def next_city_data(request: Request):
    timezones_names = [timezones_data[i]['timezone'] for i in range(len(timezones_data))]
    datetime_420 = datetime.now().replace(hour=16, minute=20, second=0, microsecond=0)
    datetime_420 = datetime_420.time()
    closest_tz = find_next_timezone(timezones_names)
    local_time = datetime.now(pytz.timezone(closest_tz))
    local_time = local_time.replace(microsecond=0)
    local_time = local_time.replace(second=0)
    local_time = local_time.time()
    i = timezones_names.index(closest_tz)
    minutes_to_420 = (datetime_420.hour - local_time.hour) * 60 + (datetime_420.minute - local_time.minute)
    is_420 = False
    if local_time >= datetime_420 and local_time <= datetime.strptime("16:30", "%H:%M").time():
        is_420 = True
    return {
        'map_img': timezones_data[i]['map'],
        'city': timezones_data[i]['city'],
        'country': timezones_data[i]['country'],
        'timezone': timezones_data[i]['timezone'],
        'desc': timezones_data[i]['desc'],
        'sub_desc': timezones_data[i]['subdesc'],
        'pop_count': timezones_data[i]['population'],
        'minutes_to_420': minutes_to_420,   
        'is_420': is_420,
    }

def closest_timezone(timezones, target_time):
    now = datetime.now()
    target_time = datetime.combine(now, target_time)
    next_target_time = target_time if now <= target_time else target_time + timedelta(days=1)
    closest_timezone = None
    closest_diff = None
    for tz in timezones:
        tz_time = datetime.now(timezone(tz)).time()
        tz_datetime = datetime.combine(now, tz_time)
        tz_datetime = tz_datetime.replace(microsecond=0)
        if tz_datetime > next_target_time:
            diff = (tz_datetime - next_target_time).total_seconds()
            if closest_diff is None or diff < closest_diff:
                closest_diff = diff
                closest_timezone = tz
    return closest_timezone

def find_next_timezone(timezones, target_time=datetime.strptime("16:20", "%H:%M").time()):
    limit_time = datetime.strptime("16:30", "%H:%M").time()
    for timezone in timezones:
        tz = pytz.timezone(timezone)
        current_tz_time = datetime.now(tz).time()
        # check if current time is between 16:20 and 16:30
        if current_tz_time >= target_time and current_tz_time <= limit_time:
            return timezone
    closest_timezone = None
    closest_time_diff = None
    for timezone in timezones:
        tz = pytz.timezone(timezone)
        current_tz_time = datetime.now(tz).time()
        if current_tz_time < target_time:
            current_tz_datetime = datetime.combine(datetime.now().date(), current_tz_time)
            target_datetime = datetime.combine(datetime.now().date(), target_time)
            # calculate time diff
            time_diff = target_datetime - current_tz_datetime
            if closest_time_diff is None or time_diff < closest_time_diff:
                closest_time_diff = time_diff
                closest_timezone = timezone
    return closest_timezone


