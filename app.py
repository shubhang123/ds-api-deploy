from fastapi import FastAPI
from pydantic import BaseModel
import random
import json

app = FastAPI()

# POST request body schema
class College(BaseModel):
    Size: int
    Mean: float
    Median: int
    Mode: int
    Min: int
    Max: int
    Secret: int

# GET /input route (Step 1)
@app.get("/input")
def college_data(email: str):
    numbers = [1, 70, 80, 20, 90, 30]  # Simulated list
    secret_key = random.randint(1000000000, 9999999999)  # Random 10-digit key

    return {
        "email": email,
        "Data": numbers,   
        "Secret": secret_key
    }

# POST /submit route (Step 2)
@app.post("/submit")
def submit_data(item: College, email: str):
    return {
        "message": "Your response has been submitted successfully",
        "email": email,
        "received": item
    }
