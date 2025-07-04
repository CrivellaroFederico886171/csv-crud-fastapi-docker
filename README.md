# csv-crud-fastapi-docker

## main.py
File che permette l'implementazione delle operazioni CRUD con FastAPI su un CSV, quindi permette:

- l'inserimento di un recordo tramite def create_item(record: Record)
- la lettura di tutti i record tramite def get_all_records()
- la visualizzazione di un singolo record con def get_record(item_id: int)
- per la modifica di un record si usa def update_record_route(item_id: int, updated_record: Record)
- la cancellazione di un record con def delete_item_route(item_id: int)
- la conta del numero di record con la funzione def get_count()

Tutte queste operazioni prevedono la lettura e scrittura all'interno del file csv data.csv, che viene effettuata tramite il file csv_handler.py

## csv:handler.py
Qui ci sono tutte le funzioni che operano direttamente su data.csv, che verranno poi richiamate all'interno di main.py

- def read_all_records() serve per aprire data.csv in fase di sola lettura, questa funzione ci ritorna tutti i record salvati nel file
- def read_record(record_id: int) legge un singolo record partendo dall'id, che è univoco. si appoggia a read_all_records() per aprire data.csv
- def write_all_records(records: list) apre data.csv in modalità read, viene usato per le operazioni di delite, WRITEput e update
- def write_record(record: dict) aggiunge a data.csv un singolo record, se non ha un id già esistente
- def delete_record(record_id: int) cancella un record specifico da data.csv in base all'id in input
- def update_record(item_id: int, updated_item: dict) cambia i valori di un record già esistente con quelli dati in input
- def count_records() ritorna il numero di record nel file

## data.csv
Contiene tutti i record che verranno salvati, è composto dalle colonne ID, NOME, COGNOME, CODICE_FISCALE

## dockerfile
Serve per poter collegare il progetto all'immagine docker