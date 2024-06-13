# User: read sg_90k_part1.json and show the first object
import json
with open('/Volumes/LaCie/ShareGPT/sg_90k_part1.json', 'r') as file:
    data = json.load(file)
print(json.dumps(data[0], indent=4))
