from fastapi import FastAPI 

from server.routes.todo_item import router as TodoItemRouter

app = FastAPI()

app.include_router(TodoItemRouter, tags = ["TodoItem"], prefix = "/todo_item")

@app.get('/', tags = ["Root"])
async def read_root():
    return {"message": "Welcome to Todo App!"}
