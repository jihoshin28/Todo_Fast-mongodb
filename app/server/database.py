import motor.motor_asyncio
import bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = 
{
    "todo_items": client.todo_items,
    "users": client.users
}

todo_items_collection = database.todo_items.get_collection("todo_items_collection")
users_collection = database.users.get_collection("users_collection")

def todo_item_helper(todo_item) -> dict:
    return{
        "item": todo_item["item"],
        "title": todo_item["title"]
    }

def user_helper(user) -> dict:
    return{
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "email": user["email"],
    }