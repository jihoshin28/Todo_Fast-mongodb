from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field

class TodoItemSchema(BaseModel):
    _id: ObjectId
    item: str
    title: str 
    class Config:
        schema_extra = {
            "example": {
                "item": "Item 1",
                "title": "Title 1"
            }
        }

class UpdateTodoItemModel(BaseModel):
    item: Optional[str]
    title: Optional[str]
    class Config:
        schema_extra = {
            "example": {
                "item": "Updated To Item 1",
                "title": "Updated To Title 1"
            }
        }

def ResponseModel(data, message):
    return{
        "data": data,
        "code": 200,
        "message": message
    }

def ErrorResponseModel(error, code, message):
    return{"error": error, "code": code, "message": message}
