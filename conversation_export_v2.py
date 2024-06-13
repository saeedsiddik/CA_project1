# User: read sg_90k_part1.json and show the first object
import json
with open('/Volumes/LaCie/ShareGPT/sg_90k_part1.json', 'r') as file:
    data = json.load(file)
print(json.dumps(data[0], indent=4))

# User: read sg_90k_part1.json and show the first object
import json
with open('/Volumes/LaCie/ShareGPT/sg_90k_part1.json', 'r') as file:
    data = json.load(file)
print(json.dumps(data[0], indent=4))

# Attempted chunk reading:
import json
with open('/Volumes/LaCie/ShareGPT/sg_90k_part1.json', 'r') as file:
    content = file.read()
    data = json.loads(content[:5000])
print(json.dumps(data[0], indent=4))

# User: How many objects are there?
file_path = '/Volumes/LaCie/ShareGPT/sg_90k_part1.json'
with open(file_path, 'r') as file:
    data = json.load(file)
print(f'Total number of objects: {len(data)}')
