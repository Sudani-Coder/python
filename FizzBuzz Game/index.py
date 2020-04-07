def FizzBuzz(TheInput):
    if TheInput in range(1, 50):
        if TheInput % 3 == 0 and TheInput % 5 == 0:
            return "\nFizzBuzz"

        elif TheInput % 3 == 0:
            return "\nFizz"
        
        elif TheInput % 5 == 0:
            return "\nBuzz"
        
        else:
            return "\n{}".format(TheInput)

    else:
        return "\nplease enter a number between 1 and 50"

while True:
    UserInput = eval(input("\nplease enter a number in range from 1 to 50 --> "))
    print(FizzBuzz(UserInput))
