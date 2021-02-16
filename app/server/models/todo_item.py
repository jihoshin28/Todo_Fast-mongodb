from typing import Optional

from pydantic import BaseModel, EmailStr, Field

class TodoItemSchema(BaseModel):
    item: str = Field(...)
    title: str = Field(...)
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "item": "Item 1",
    #             "title": "Title 1"
    #         }
    #     }

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
