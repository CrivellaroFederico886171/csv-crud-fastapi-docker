from fastapi import FastAPI, HTTPException
from csv_handler import *
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    nome: str
    cognome: str
    codice_fiscale: str

@app.post("/items/")
def create_item(item: Item):
    if read_item(item.id):
        raise HTTPException(status_code=400, detail="ID già esistente")
    write_item(item.dict())
    return item

@app.get("/items/")
def get_all_items():
    return read_all_items()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = read_item(item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item non trovato")

@app.put("/items/{item_id}")
def update_item_route(item_id: int, item: Item):
    if not read_item(item_id):
        raise HTTPException(status_code=404, detail="Item non trovato")
    update_item(item_id, item.dict())
    return item

@app.delete("/items/{item_id}")
def delete_item_route(item_id: int):
    if not read_item(item_id):
        raise HTTPException(status_code=404, detail="Item non trovato")
    delete_item(item_id)
    return {"message": "Item deleted successfully"}

@app.get("/items/count")
def get_count():
    return {"count": count_items()}
