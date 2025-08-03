from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo de item
class Item(BaseModel):
    name: str
    price: float

# Lista em memória
items: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API FastAPI!"}

@app.get("/items")
def list_items():
    return items

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return {"message": "Item adicionado", "item": item}
