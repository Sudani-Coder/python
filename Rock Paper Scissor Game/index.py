## project11
# Rock - Paper - Scissor "Game"

import random
print(
    """
    Winning Rules:  \n
    "Rock vs paper => paper wins" \n
    "Rock vs scissor => Rock wins" \n
    "paper vs scissor => scissor wins \n
    """
)

# Step 1: Conditions for the User
while True:
    print("\nEnter Choice 1.Rock 2.Paper 3.Scissor", end = "\n\n")
    user_choice = int(input("User Turn --> "))
    while user_choice > 3 or user_choice < 1:
        user_choice = int(input("\nEnter valid input --> "))
    
    if user_choice == 1:
        user_choice_name = "Rock"
    elif user_choice == 2:
        user_choice_name = "Paper"
    else:
        user_choice_name = "Scissor"
    
    print("\nUser choice is : {}".format(user_choice_name), end = "\n\n")
    print("It's computer turn --> ", end = "\n\n")

    # Step 2: Conditions for the Computer
    computer_choice = random.randint(1, 3)
    while computer_choice == user_choice:
        computer_choice = random.randint(1, 3)

    if computer_choice == 1:
        computer_choice_name = "Rock"
    elif computer_choice == 2:
        computer_choice_name = "Paper"
    else:
        computer_choice_name = "Scissor"

    print("Computer choice is : {}".format(computer_choice_name), end = "\n\n")
    print(user_choice_name + " VS " + computer_choice_name, end = "\n\n")

    # Step 3: Condition of Winning !!!
    if ((user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1)):
        print("paper wins => ", end = "")
        result = "Paper"
    elif ((user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 2)):
        print("scissor wins => ", end = "")
        result = "Scissor"
    else:
        print("rock wins => ", end = "")
        result = "Rock"

    # Step 4: Printing the Winner
    if result == user_choice_name:
        print("<** User wins **>")
    else:
        print("<** Computer wins **>")

    print("\nDo you want to play again? (Y/N):", end=" ")
    answer = input()
    print("\n\n========================================================================================\n")

    # if user input n or N then Break
    if answer == "n" or answer == "N":
        break

print("\nThanks for playing", end = "\n\n")