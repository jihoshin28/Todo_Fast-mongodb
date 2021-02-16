from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_todo_item,
    delete_todo_item,
    retrieve_todo_item,
    retrieve_todo_items,
    update_todo_items
)

from app.server.models.todo_item{
    ErrorResponseModel,
    ResponseModel,
    TodoItemSchema,
    UpdateTodoItemModel
}

router = APIRouter()

@router.post('/', response_description = "To do data added into the database")
async def add_todo_item(todo_item: TodoItemSchema = Body(...)):
    todo_item = jsonable_encoder(todo_item)
    new_todo_item = await add_todo_item(todo_item)
    return ResponseModel(new_todo_item, "To do item added successfully")