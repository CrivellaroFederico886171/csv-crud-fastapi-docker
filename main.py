from fastapi import FastAPI, HTTPException
from csv_handler import *
from pydantic import BaseModel

app = FastAPI()


class Record(BaseModel):
    id: int
    nome: str
    cognome: str
    codice_fiscale: str

@app.get("/")
def root():
    return {"message": "Welcome to the CSV CRUD API"}

# Endpoint per la creazione di un nuovo record
@app.post("/items/")
def create_item(record: Record):
    exst_record = read_record(record.id)
    if exst_record:
        raise HTTPException(status_code=400, detail="Record già esistente")
    write_record(record.model_dump())
    return {"message": "Record creato correttamente", "record": record}

# Endpoint per ottenere tutti i record
@app.get("/items/")
def get_all_records():
    records = read_all_records()
    if not records:
        raise HTTPException(status_code=404, detail="Nessun record trovato")
    return records

# Endpoint per ottenere un singolo record basato sull'ID
@app.get("/items/{item_id}")
def get_record(item_id: int):
    record = read_record(item_id)
    if not record:
        raise HTTPException(status_code=404, detail="Record non trovato")
    return record

# Endpoint per aggiornare un record esistente
@app.put("/items/{item_id}")
def update_record(item_id: int, updated_record: Record):
    existing_record = read_record(item_id)
    if not existing_record:
        raise HTTPException(status_code=404, detail="Record non trovato")
    updated_record.id = item_id

# Endpoint per eliminare un record esistente
@app.delete("/items/{item_id}")
def delete_record(item_id: int):
    existing_record = read_record(item_id)
    if not existing_record:
        raise HTTPException(status_code=404, detail="Record non trovato")
    delete_record(item_id)
    return {"message": "Record eliminato correttamente"}

# Endpoint per ottenere il numero di righe nel CSV
@app.get("/items/count")
def count_records():
    count = count_records()
    return {"count": count}
