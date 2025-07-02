import csv

CSV = "data.csv"

# Funzioni per la gestione del CSV

# Funzione per leggere tutti i record
def read_all_records():
    with open(CSV, mode="r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

# Funzione per leggere un singolo record basato sull'ID
def read_record(record_id: int):
    records = read_all_records()
    for record in records:
        if int(record["id"]) == record_id:
            return record
    return None

# Funzione per la scrittura dei record
def write_all_records(records: list):
    with open(CSV, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "nome", "cognome", "codice_fiscale"])
        writer.writeheader()
        writer.writerows(records)

# Funzione per scrittura di un singolo record
def write_record(record: dict):
    records = read_all_records()
    records.append(record)
    write_all_records(records)

# Funzione per eliminare un record basato sull'ID
def delete_record(record_id: int):
    records = read_all_records()
    new_records = [record for record in records if int(record["id"]) != record_id]
    write_all_records(new_records)

# Funzione per aggiornare un record esistente
def update_record(record_id: int, updated_record: dict):
    records = read_all_records()
    for i, record in enumerate(records):
        if int(record["id"]) == record_id:
            records[i] = updated_record
            break
    write_all_records(records)

# Funzione per contare il numero di record
def count_records():
    return len(read_all_records())