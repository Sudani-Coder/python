import json

people_string = '''
{
    "people": [
        {
            "name": "SudaniCoder",
            "age": 21,
            "gender": "Male",
            "mobile": "0123456789",
            "emails": [
                "Sudani.Coder_1999@gmail.com",
                "omer@enayatech.com"
            ],
            "languages": [
                "HTML",
                "CSS",
                "JS",
                "PY",
                "SQL"
            ],
            "has_license": true
        },
        {
            "name": "RootAdmin",
            "age": 19,
            "gender": "female",
            "mobile": "9876543210",
            "emails": null,
            "languages": [
                "HTML",
                "CSS",
                "JS",
                "PY",
                "SQL"
            ],
            "has_license": false
        }
    ]
}
'''

data = json.loads(people_string)

print(type(data))
print(type(data['people']))

for person in data['people']:
    print(person, end='\n\n')

for person in data['people']:
    del person['languages']

new_data = json.dumps(data, indent=2)

print(type(new_data))
print(new_data)
