## project 12: Checking the validity of password

# Validation Criteria :

# At least 1 letter between [a-z]
# At least 1 letter between [A-Z]
# At least 1 number between [0-9]
# At least 1 character from [@#$_]
# Minimum length 8 characters
# Maximum length 28 characters

import re

passwd = input("Enter your Password --> ")

X = True

while X:
    if (len(passwd) < 8 or len(passwd) > 28):
        break
    elif not re.search("[a-z]", passwd):
        break
    elif not re.search("[A-Z]", passwd):
        break
    elif not re.search("[0-9]", passwd):
        break
    elif not re.search("[@#$_]", passwd):
        break
    else:
        print("Valid Password !!!")
        X = False
        break

if X:
    print("Not a Valid Password !!!")