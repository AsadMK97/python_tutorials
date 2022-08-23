import json


with open("data_tutorial/uk.json", "r") as json_file:
    json_data = json.load(json_file)


print(json_data["places"])

places = [{'name': 'Edinburgh', 'x': 55.953251, 'y': -3.188267}, {'name': 'York', 'x': 53.958332, 'y': -1.080278}, {'name': 'Salford', 'x': 53.483002, 'y': -2.2931},
{'name': 'Perth', 'x': 56.396999, 'y': -3.437}, {'name': 'Newcastle', 'x': 54.966667, 'y': -1.6}, {'name': 'Dundee', 'x': 56.462002, 'y': -2.9707}, 
{'name': 'Liverpool', 'x': 53.400002, 'y': -2.983333}, {'name': 'Glasgow', 'x': 55.860916, 'y': -4.251433}, {'name': 'Oxford', 'x': 51.752022, 'y': -1.257677},
{'name': 'London', 'x': 51.509865, 'y': -0.118092}, {'name': 'Aberdeen', 'x': 57.149651, 'y': -2.099075}, {'name': 'Manchester', 'x': 53.483959, 'y': -2.244644},
{'name': 'Inverness', 'x': 57.477772, 'y': -4.224721}]

places_dict = {}
for place in places:
    places_dict[place["name"].lower()]={"latitude": place["x"], "longitude": place["y"]}


user_input = input("Enter a city or town: ").lower()

try:
    new_place = places_dict[user_input]
except Exception:
    print(user_input + " does not exist")
    exit(0)
print(new_place)