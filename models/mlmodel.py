
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MLModel(BaseModel):
    id: Optional[str]
    name: str
    model_type: Optional[str]
    model_s3_route: str
    framework: Optional[str]
    created_at: datetime = datetime.now()
    active: bool = True