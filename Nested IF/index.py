uName = input("what's your name? ").strip().capitalize()
uCountry = input("what's your country? ").strip().lower()
isStudent = input("Are You Student(yes or no)? ").strip().lower()
cName = "Python Basic's"
cPrice = 100
cDiscount = None

if uCountry == "sudan" or uCountry == "south sudan":

    if isStudent == "yes":
        cDiscount = 60
        print(f"Hello {uName} because you are from {uCountry} and student")
        print(f"The course \"{cName}\" price is: ${cPrice - cDiscount}")

    elif isStudent == "no":
        cDiscount = 50
        print(f"Hello {uName} because you are from {uCountry}")
        print(f"The course \"{cName}\" price is: ${cPrice - cDiscount}")

elif uCountry == "egypt":

    if isStudent == "yes":
        cDiscount = 35
        print(f"Hello {uName} because you are from {uCountry} and student")
        print(f"The course \"{cName}\" price is: ${cPrice - cDiscount}")

    elif isStudent == "no":
        cDiscount = 25
        print(f"Hello {uName} because you are from {uCountry}")
        print(f"The course \"{cName}\" price is: ${cPrice - cDiscount}")

elif uCountry == "ksa" or uCountry == "uae":

    if isStudent == "yes":
        cDiscount = 25
        print(f"Hello {uName} because you are from {uCountry} and student")
        print(f"The course \"{cName}\" price is: ${cPrice - cDiscount}")

    elif isStudent == "no":
        cDiscount = 15
        print(f"Hello {uName} because you are from {uCountry}")
        print(f"The course \"{cName}\" price is: ${cPrice - cDiscount}")

else:

    if isStudent == "yes":
        cDiscount = 15
        print(f"Hello {uName} because you are from {uCountry} and student")
        print(f"The course \"{cName}\" price is: ${cPrice - cDiscount}")

    elif isStudent == "no":
        cDiscount = 10
        print(f"Hello {uName} because you are from {uCountry}")
        print(f"The course \"{cName}\" price is: ${cPrice - cDiscount}")

movieRate = 18
age = 18
print("Movie Is Not Good 4U" if age < movieRate else "Movie Is Good 4U")
