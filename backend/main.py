from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI(title="MentEcológica API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4321", "https://mentecologica.netlify.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

@app.get("/api/co2")
async def get_co2():
    df = pd.read_csv(os.path.join(DATA_DIR, "co2-emissions.csv"))
    csv_data = df.to_csv(index=False)
    return df.to_dict(orient="records")

@app.get("/api/temperature")
async def get_temperature():
    df = pd.read_csv(os.path.join(DATA_DIR, "temperature-mexico.csv"))
    csv_data = df.to_csv(index=False)
    return df.to_dict(orient="records")

@app.get("/")
async def root():
    return {"message": "API JSON lista"}