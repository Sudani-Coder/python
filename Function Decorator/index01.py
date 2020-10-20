def myDecorator(func):
    def nestedFunc(*numbers):
        for number in numbers:
            if number < 0:
                print("Beware one or more of the numbers is less than zero")

        print("Before")
        func(*numbers)
        print("After")
    return nestedFunc

def myDecoratorTwo(func):
    def nestedFunc(*numbers):
        print("Hello world from decorator two")
        func(*numbers)
    return nestedFunc

@myDecoratorTwo
@myDecorator
def calculate(num1, num2, num3) -> int:
    print(num1 + num2 + num3)

calculate(-32, 128, -64)
