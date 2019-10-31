## project: 9
# text analyzer
vowels = ("a", "e", "i", "o", "u")

def count_char(text, char):
    count = 0
    for each in text:
        if each == char:
            count += 1
    return count

def count_vowels(text):
    count = 0
    for each in text:
        if each in vowels:
            count += 1
    return count

def perc_char(text):
    for char in "abcdefghijklmnopqrstuvwxyz":
        perc = 100 * count_char(text, char) / len(text)
        print("{0} - {1}%".format(char, round(perc, 2)))

filename = input("Please Enter The File Name -->")
thechar = input("Please Enter The char -->").lower()
with open(filename, "rt") as myfile:
    text = myfile.read()

print("the char {} repeted {} number of times".format(thechar ,count_char(text, thechar)))
print("the number of vowels letters is {}".format(count_vowels(text)))
perc_char(text)