from http import client
from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root(request: Request):
    client_ip = request.client.host
    # get timezone of ip    
    conn = client.HTTPConnection("ip-api.com")
    conn.request("GET", "/json/" + client_ip)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    data = data.decode("utf-8")
    data = eval(data)
    timezone = data["timezone"]

    return {"timezone": timezone}


