import json
import os

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
        "notes": notes
    }
    data = load_entries()
    data.append(entry)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
