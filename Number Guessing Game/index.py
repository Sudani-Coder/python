## Project: 4
# Number Guessing game

import random

guess = []
cpu_num = random.randint(1, 100)
player_num = int(input("Please Enter A Number Between 1 To 100 --> "))
guess.append(player_num)

while player_num != cpu_num:
    if player_num > cpu_num:
        print("Too High !")
    else:
        print("Too Low !")

    player_num = int(input("Please Enter A Number Between 1 To 100 --> "))
    guess.append(player_num)

else:
    print("Well Done !!!")
    print("You Have Taken {} Guesses".format(len(guess)))
    print("Here Are Your Guesses : ")
    print(guess)