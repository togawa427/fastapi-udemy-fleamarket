from fastapi import FastAPI
from cruds import item as item_cruds


app = FastAPI()


@app.get("/items")
async def find_all():
    return item_cruds.find_all()

@app.get("/items/{id}")
async def find_by_id(id: int):
    return item_cruds.find_by_id(id)

@app.get("/items/") # 一覧取得の/itemsを上書きしないようにするため最後に / をつける
async def find_by_name(name: str):
    return item_cruds.find_by_name(name)