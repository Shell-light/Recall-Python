import os
from fastapi import FastAPI
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Day 17
CASHE_DIR = os.path.join(BASE_DIR, 'cashe')

dataset = os.path.join(CASHE_DIR, 'movies-box-office-dataset-cleaned.csv')

app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get('/box-office')
def read_box_office_numbers():
    df = pd.read_csv(dataset)
    return df.to_dict("Rank")