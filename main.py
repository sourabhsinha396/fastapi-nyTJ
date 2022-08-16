import os
from typing import Optional
from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()

@app.get("/")
def read_index():
    return {"message":"append any city name to the url after / e.g. www.url.com/pune"}

@app.get("/{city}")
def read_root(city:str):
    try:
        token = os.getenv("openweather_token")
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}")
        print(response.json())
        return response.json().get('weather')[0]["main"]
    except:
        return {"message":"Please enter valid city name"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", default=5000)), log_level="info")
