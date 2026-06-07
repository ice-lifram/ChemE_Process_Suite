import json
import os

# Get the path to the directory where this file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "elements.json")

def load_molar_masses():
    try:
        with open(JSON_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The data file {JSON_PATH} was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: The data file {JSON_PATH} contains invalid JSON.")
        return {}

# This maintains the variable name so that other modules (like the parser and logic.py)
# don't need to be changed. They still access the dictionary via 'elements_molarmass'.
elements_molarmass = load_molar_masses()
