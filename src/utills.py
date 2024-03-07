import json

def add_initial_data():
    with open("operations.json","wt") as file:
        initial_data = json.loads(file)
        return initial_data


add_initial_data()
