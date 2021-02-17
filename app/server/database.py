import motor.motor_asyncio
from bson import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.todo_items
# {
#     "_todo_items": client.todo_items,
#     "_users": client.users
# }

todo_item_collection = database.todo_items_collection
# users_collection = database.users.get_collection("users_collection")

def todo_item_helper(todo_item) -> dict:
    return{
        "id": str(todo_item["_id"]),
        "item": todo_item["item"],
        "title": todo_item["title"]
    }

def user_helper(user) -> dict:
    return{
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "email": user["email"],
    }

async def retrieve_todo_items():
    todo_items = []
    async for todo_item in todo_item_collection.find():
        todo_items.append(todo_item_helper(todo_item))
    return todo_items

async def add_todo_item(todo_item_data: dict) -> dict:
    todo_item = await todo_item_collection.insert_one(todo_item_data)
    new_todo_item = await todo_item_collection.find_one({"_id": todo_item.inserted_id})
    return todo_item_helper(new_todo_item)

async def retrieve_todo_item(id: str) -> dict:
    todo_item = await todo_item_collection.find_one({"_id": ObjectId(id)})
    if todo_item:
        return todo_item_helper(todo_item)

async def update_todo_item(id: str, data: dict):
    if len(data) < 1:
        return False
    todo_item = await todo_item_collection.find_one({"_id": ObjectId(id)})
    if todo_item:
        updated_todo_item = await todo_items_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_todo_item:
            return True
        return False 

async def delete_todo_item(id: str):
    todo_item = await todo_item_collection.find_one({"_id": ObjectId(id)})
    if todo_item:
        await student_collection.delete_one({"_id": ObjectId(id)})
        return True