import csv

CSV = "data.csv"

def read_all_items():
    with open(CSV, mode="r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def read_item(item_id: int):
    items = read_all_items()
    for item in items:
        if int(item["id"]) == item_id:
            return item
    return None

def write_item(item: dict):
    items = read_all_items()
    items.append(item)
    write_all_items(items)

def write_all_items(items: list):
    with open(CSV, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "nome", "cognome", "codice_fiscale"])
        writer.writeheader()
        writer.writerows(items)

def delete_item(item_id: int):
    items = read_all_items()
    new_items = [item for item in items if int(item["id"]) != item_id]
    write_all_items(new_items)

def update_item(item_id: int, updated_item: dict):
    items = read_all_items()
    for i, item in enumerate(items):
        if int(item["id"]) == item_id:
            items[i] = updated_item
            break
    write_all_items(items)

def count_items():
    return len(read_all_items())