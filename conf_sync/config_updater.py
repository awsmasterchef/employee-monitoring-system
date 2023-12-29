import json
import os


def update_configuration(updated_data):
    with open("../config.json", "r") as file:
        data = json.load(file)
    for key, value in updated_data.items():
        data[key] = value
    with open(f"../config.json", 'w') as file:
        json.dump(data, file, indent=2)
    print("Configuration Update Sucessfully")