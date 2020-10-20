peoples = ["osama", "ahmed", "omer", "ali"]

skills = ["HTML", "CSS", "JS", "PY", "SQL"]

for person in peoples: # Outer Loop

    print(f"\n{person.capitalize()} skills is:")

    for skill in skills: # Inner Loop

        print(f"\n- {skill}")
