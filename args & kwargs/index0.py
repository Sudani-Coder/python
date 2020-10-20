WebSkills = ("HTML", "CSS", "JS")

MySkills = {
    "GIT": "90%",
    "LINUX": "80%",
    "DJANGO": "95%",
    "BOOTSTRAP": "85%",
    "UML": "75%"
}

def show_skills(name, *skills, **skillsProgress):
    print(f"\nHello {name}")

    print("\nskills without progress: ")
    for skill in skills:
        print(f"\n- {skill}")
    
    print("\nskills with progress: ")
    for skill_key, skill_value in skillsProgress.items():
        print(f"\n- {skill_key} => {skill_value} ")

show_skills("Omer", *WebSkills, "XML", PY = "100%", SQL = "70%", **MySkills)
