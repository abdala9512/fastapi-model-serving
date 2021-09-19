from fastapi import FastAPI



from routes.mlmodel import mlmodel

app = FastAPI()

app.include_router(mlmodel)