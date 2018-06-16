import json


dict_data = json.load(open("data.json"))

print(dict_data["rain"][0])