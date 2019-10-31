## project: 8
# function as object
def add(x, y):
    return x + y

def do_twice(func, x, y):
    return func(func(x, y), func(x, y))

num1 = int(input(" \nEnter first number: "))
num2 = int(input(" \nEnter second number: "))

print("\nThe result =", do_twice(add, num1, num2), end="\n\n")