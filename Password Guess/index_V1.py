tries = 4

mainPassword = "RootAdmin"

inputPassword = input("\nPlease Enter Your Password --> ")

while inputPassword != mainPassword and tries > 0:
    tries -= 1

    print(f"\nWrong Password, { 'Last' if tries == 0 else tries } Chance Left")

    inputPassword = input("\nPlease Enter Your Password --> ")

else:
    if inputPassword == mainPassword:
        print("\nCorrect Password")

    else:
        print("\nAll Tries Is Finished")
