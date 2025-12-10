
import time
import httpx
from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/")
def greet_json():
    return {"Hello": "World!"}
