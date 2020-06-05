manatees = [
    {
        "name": "softy",
        "age": 5,
    },
    {
        "name": "fluffy",
        "age": 15,
    },
    {
        "name": "smoothie",
        "age": 10,
    },
]

def PrintManatees(manatees):
    for manatee in manatees:
        print()
        for manatee_property in manatee:
            print(manatee_property, ":", manatee[manatee_property])

PrintManatees(manatees)
