

def mlmodel_entity(item) -> dict:
    return {
        "id": str(item['_id']),
        "name": item['name'],
        "model_type": item['model_type'],
        "model_s3_route": item['model_s3_route'],
        "framework": item['framework'],
        "created_at": item['created_at'],
        "active": item['active']

    }


def mlmodels_entity(entity) ->  list:
    return [mlmodel_entity(item) for item in entity]