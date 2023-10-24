from fastapi import FastAPI
from typing import List

from backend.models.item import Item


app = FastAPI()


items: List[Item] = [
    Item(id=1, name="Item 1", price=9.99),
    Item(id=2, name="Item 2", price=19.99),
    Item(id=3, name="Item 3", price=29.99),
    Item(id=4, name="Item 4", price=39.99),
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    return {"message": "Item not found"}


@app.get("/items/")
async def read_items():
    return items


@app.post("/items/")
async def create_item(item: Item):
    items.append(item)
    return {"message": "Item created"}
