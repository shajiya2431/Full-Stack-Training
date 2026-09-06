import json
def save_data(data):

    with open("student.json", "w") as file:
        json.dump(data, file, indent=4)

def Load_data():
    with open("student.json", "r") as file:
        return json.load(file)