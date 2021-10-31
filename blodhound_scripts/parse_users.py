import json
data = json.load(open('data.json'))
for node in data["nodes"]:
    print(node["props"]["name"])