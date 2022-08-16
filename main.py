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
        import random
        lis = ["cloudy","clear sky","hazy","rainy",]
        return {f"the weather of {city} looks":random.choice(lis)}
    except:
        return {"message":"Please enter valid city name"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", default=5000)), log_level="info")
