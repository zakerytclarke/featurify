# fastapi_app/main.py
from fastapi import FastAPI
from library.some_module import some_function  # Importing from your library

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/use_library")
def use_library_function():
    result = some_function()  # Using a function from your custom library
    return {"result": result}
