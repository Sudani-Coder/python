def locate_all(string, sub):
    matches = []
    index = 0
    while index < len(string):
        if string[index : index + len(sub)] == sub:
            matches.append(index)
            index += len(sub)

        else:
            index += 1

    return matches

print(locate_all("hello world lo", "lo"))
print("hello world lo".find("lo"))
