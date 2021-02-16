from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    firstname: str = Field(...)
    lastname: str = Field(...)
    email: EmailStr = Field(...)
    
class UpdateUserModel(BaseModel):
    firstname: Optional[str]
    lastname: Optional[str]
    email: Option[EmailStr]

def ResponseModel(data, message):
    return{
        "data": data,
        "code": 200,
        "message": message
    }

def ErrorResponseModel(error, code, message):
    return{"error", "code": code, "message": message}