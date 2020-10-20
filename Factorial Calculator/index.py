## project: 6
# recursion function (factorial calculator)

num = int(input("Please Enter The Number --> "))

def factorial(num):
    if num == 1:
        return 1

    else:
        return num * factorial(num - 1)

print("\nThe Factorial Of {} Is => {}".format(num, factorial(num)))
