import json, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state, end='\n\n')

for state in data['states']:
    del state['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)
