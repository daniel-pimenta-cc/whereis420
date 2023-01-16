from http import client
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
from data import timezones
import pytz
import json
templates = Jinja2Templates(directory="templates/")


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root(request: Request):
    
    #get timezone of the request
    client_ip = pytz.timezone(request.headers.get("Timezone", "UTC"))
    client_host = request.client.host
    br_counter += 1

    print(client_host)
    
    for i in range(len(timezones)):
        local_time = datetime.now(pytz.timezone(timezones[i]['timezone']))
        four_20_pm = local_time.replace(hour=16, minute=20, second=0, microsecond=0)
        four_30_pm = local_time.replace(hour=16, minute=30, second=0, microsecond=0)
        three_30_pm =  local_time.replace(hour=15, minute=30, second=0, microsecond=0)
        
        if local_time > four_20_pm and local_time < four_30_pm:
            return templates.TemplateResponse("index.html", {"request": request, 'text': f'Is 4:{local_time.minute} in {timezones[i]["city"]}, {timezones[i]["country"]}', 'content': json.dumps(timezones[i])})
            
        elif local_time < four_20_pm and local_time > three_30_pm:
            if local_time.hour == 15:
                minutes_to_420 = (60 - local_time.minute) + 20
            else:
                minutes_to_420 = 20 - local_time.minute
            return templates.TemplateResponse("index.html", {"request": request, 'text': f'It will be 4:20 in {timezones[i]["city"]}, {timezones[i]["country"]} in {minutes_to_420} minutes', 'content': json.dumps(timezones[i])})
            
    
    
    minutes_to_420 = 20 - local_time.minute       
    return templates.TemplateResponse("index.html", {"request": request, 'text': f'It will be 4:20 in {timezones[0]["city"]}, {timezones[0]["country"]} in {minutes_to_420} minutes', 'content': json.dumps(timezones[0])})
        
@app.get("/v2")
async def root(request: Request):
    i = 0
    local_time = datetime.now(pytz.timezone(timezones[i]['timezone']))
    
    minutes_to_420 = 20 - local_time.minute       
    return templates.TemplateResponse("index.html", 
    {
        "request": request,
        'text': f'It will be 4:20 in {timezones[i]["city"]}, {timezones[i]["country"]} in {minutes_to_420} minutes',
        'map_img': timezones[i]['map'],
        'city': timezones[i]['city'],
        'country': timezones[i]['country'],
        'timezone': timezones[i]['timezone'],
        'desc': timezones[i]['desc'],
        'sub_desc': timezones[i]['subdesc'],
        'pop_count': timezones[i]['population']['count'],
        'current_hour': local_time.hour,
        'current_minute': local_time.minute,
        'minutes_to_420': minutes_to_420,
        'content': json.dumps(timezones[i])
    })
        
