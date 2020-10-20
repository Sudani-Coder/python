import re

is_email = re.search(r"^[A-z0-9\.]+@\w+\.\w{2,4}$", "Sudani.Coder_1999@gmail.info")

if is_email:
    print("Good")
    print(is_email.span())
    print(is_email.string)
    print(is_email.group())

else:
    print("Bad")

print("#" * 50)

email_input = input("Please Write Your Email => ")

search = re.findall(r"^[A-z0-9\.]+@\w+\.\w{2,4}$", email_input)

email_list = []

if search != []:
    email_list.append(search)
    print("Email Added")

else:
    print("Invalid Email")

for email in email_list:
    print(email)
