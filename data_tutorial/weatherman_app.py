import json


with open("data_tutorial/uk.json", "r") as json_file:
    json_data = json.load(json_file)


print(json_data)
