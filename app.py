from fastapi import FastAPI
from routes.mlmodel import mlmodel

app = FastAPI(
    title = "ML model API",
    description="Model serving framework",
    version = "0.0.1",
    
)

app.include_router(mlmodel)