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

MySkills = {
    "GO": "100%",
    "GIT": "90%",
    "LINUX": "80%",
    "DJANGO": "95%",
    "BOOTSTRAP": "85%",
    "UML": "75%"
}

def showSkills(name, *args, **kwargs):
    print(f"Hello {name} \nSkills without progress is: ")

    for skill in args:
        print(f"\n- {skill}")
    
    print("\nSkills with progress is: ")

    for name, skill in kwargs.items():
        print(f"\n{name} skills: ")
        for skill_name, skill_value in skill.items():
            print(f"\n - {skill_name} --> {skill_value}")

showSkills("Sudani Coder", *MySkills, **peoples)
