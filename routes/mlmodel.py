from fastapi import APIRouter, Response
from pydantic.utils import Obj
from config.db import conn, database

from models.mlmodel import MLModel
from schemas.mlmodel import mlmodel_entity, mlmodels_entity

from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

mlmodel = APIRouter()

@mlmodel.get('/models', response_model=list[MLModel])
def get_all_models():
    return mlmodels_entity(database.models.find())


@mlmodel.get('/models/{id}', response_model=MLModel)
def get_model(id: str):
    return mlmodel_entity(database.models.find_one({"_id": ObjectId(id)}))

@mlmodel.post('/models')
def create_model(model: MLModel):

    new_model = dict(model)

    id = database.models.insert_one(new_model).inserted_id
    document = database.models.find_one({"_id": id})

    return mlmodel_entity(document)

@mlmodel.put('/models/{id}')
def update_model(id: str, model: MLModel):

    database.models.find_one_and_update({
        "_id": ObjectId(id)
        }, {
            "$set": dict(model)
        })

    return mlmodel_entity(database.models.find_one({"_id": ObjectId(id)}))

@mlmodel.delete('/models/{id}', status_code=HTTP_204_NO_CONTENT)
def delete_model(id: str):
    mlmodel_entity(database.models.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)  