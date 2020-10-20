peoples = {
    "Osama": {
        "HTML": "53%",
        "CSS": "25%",
        "JS": "41%",
        "PY": "10%",
        "SQL": "17%"
    },
    "Ahmed": {
        "HTML": "55%",
        "CSS": "65%",
        "JS": "75%",
        "PY": "85%",
        "SQL": "95%"
    },
    "Omer": {
        "HTML": "100%",
        "CSS": "100%",
        "JS": "100%",
        "PY": "100%",
        "SQL": "100%"
    },
    "Ali": {
        "HTML": "90%",
        "CSS": "80%",
        "JS": "70%",
        "PY": "60%",
        "SQL": "50%"
    }
}

for person in peoples:

    print(f"\nSkills And Progress For {person} Is: ")

    for skill in peoples[person]:

        print(f"\n- {skill} --> {peoples[person][skill]}")

