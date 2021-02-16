from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..database import (
    add_todo_item,
    delete_todo_item,
    retrieve_todo_item,
    retrieve_todo_items,
    update_todo_item
)

from ..models.todo_item import (

    ErrorResponseModel,
    ResponseModel,
    TodoItemSchema,
    UpdateTodoItemModel
)


router = APIRouter()

@router.post('/', response_description = "To do data added into the database")
async def add_todo_item(todo_item_input: TodoItemSchema = Body(...)):
    todo_item = jsonable_encoder(todo_item_input)
    new_todo_item = await add_todo_item(todo_item)
    return ResponseModel(new_todo_item, "To do item added successfully")

@router.get("/", response_description="To do Items retrieved")
async def get_todo_items():
    todo_items = await retrieve_todo_items()
    if todo_items:
        return ResponseModel(todo_items, "To do Item data retrieved successfully")
    return ResponseModel(todo_items, "Empty list returned")


@router.get("/{id}", response_description="To do Item data retrieved")
async def get_todo_item_data(id):
    todo_item = await retrieve_todo_item(id)
    if todo_item:
        return ResponseModel(todo_item, "To do Item data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "To do Item doesn't exist.")

@router.put("/{id}")
async def update_todo_item_data(id: str, req: UpdateTodoItemModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_todo_item = await update_todo_item(id, req)
    if updated_todo_item:
        return ResponseModel(
            "To do item with ID: {} name update is successful".format(id),
            "To do item name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the to do item data.",
    )

@router.delete("/{id}", response_description="Student data deleted from the database")
async def delete_todo_item_data(id: str):
    deleted_todo_item = await delete_todo_item(id)
    if deleted_todo_item:
        return ResponseModel(
            "Student with ID: {} removed".format(id), "Student deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
    )