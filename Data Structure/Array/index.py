fruits = ["Banana", "Orange", "Apple", "Mango", "Kiwi", "Lemon", "Pineapple"]
numbers = [85, 25, 5, 15, 1, 30, 20, 90, 70, 45, 60, 40, 55, 100, 50, 95, 65, 10, 80, 75, 35]

for fruit in fruits:
    print(fruit, end = "\n\n")

for num in numbers:
    print(num)

print()
def TheMax(MyList):
    maximum = MyList[0]
    for num in MyList:
        if num > maximum:
            maximum = num
    return maximum

def TheMin(MyList):
    minimum = MyList[0]
    for num in MyList:
        if num < minimum:
            minimum = num
    return minimum

print("Maximum Number = {}".format(TheMax(numbers)), "Minimum Number = {}".format(TheMin(numbers)), sep = "\n\n", end = "\n\n")