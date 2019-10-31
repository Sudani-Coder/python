## project: 5
# simple calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Take input from the user

print("  Select operation number  ", end="\n\n")
print("  1: Add                   ", end="\n\n")
print("  2: Subtract              ", end="\n\n")
print("  3: Multiply              ", end="\n\n")
print("  4: Divide                ")

while True:
    choice = input(" \nEnter choice(1/2/3/4): ")
    num1 = int(input(" \nEnter first number: "))
    num2 = int(input(" \nEnter second number: "))

    if choice == "1":
        print("\n", num1, " + ", num2, " = ", add(num1, num2))
    elif choice == "2":
        print("\n", num1, " - ", num2, " = ", subtract(num1, num2))
    elif choice == "3":
        print("\n", num1, " * ", num2, " = ", multiply(num1, num2))
    elif choice == "4":
        print("\n", num1, " / ", num2, " = ", divide(num1, num2))
    else:
        print("\n", "Invalid Input")