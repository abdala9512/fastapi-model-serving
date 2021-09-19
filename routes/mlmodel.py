from fastapi import APIRouter
from config.db import conn, database

from models.mlmodel import MLModel
from schemas.mlmodel import mlmodel_entity, mlmodels_entity

mlmodel = APIRouter()

@mlmodel.get('/models')
def get_all_models():
    return mlmodels_entity(database.models.find())


@mlmodel.get('/models/{id}')
def get_model():
    pass

@mlmodel.post('/models')
def create_model(model: MLModel):

    new_model = dict(model)

    id = database.models.insert_one(new_model).inserted_id
    document = database.models.find_one({"_id": id})

    return mlmodel_entity(document)

@mlmodel.put('/models/{id}')
def update_model():
    pass

@mlmodel.delete('/models/{id}')
def delete_model():
    pass