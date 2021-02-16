from typing import Optional

from pydantic import BaseModel, EmailStr, Field

class TodoItemSchema(BaseModel):
    item: str = Field(...)
    title: str = Field(...)

class UpdateTodoItemModel(BaseModel):
    item: Optional[str]
    title: Optional[str]


def ResponseModel(data, message):
    return{
        "data": data,
        "code": 200,
        "message": message
    }

def ErrorResponseModel(error, code, message):
    return{"error", "code": code, "message": message}
