from fastapi import FastAPI
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Food Donation Matcher")

@app.get("/")
def home():
    return {"message": "AI Food Donation Matcher API Running"}