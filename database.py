import json
import os
from datetime import datetime

DATA_FILE = "data.json"

def load_entries():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_entry(name, email, age, notes):
    entry = {
        "name": name,
        "email": email,
        "age": age,
        "notes": notes,
        "timestamp": datetime.now().isoformat()
    }
    data = load_entries()
    data.append(entry)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def update_entry(index, name, email, age, notes):
    data = load_entries()
    data[index] = {
        "name": name,
        "email": email,
        "age": age,
        "notes": notes,
        "timestamp": data[index].get("timestamp", datetime.now().isoformat())
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def delete_entry(index):
    data = load_entries()
    if 0 <= index < len(data):
        data.pop(index)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
