tries = 4

mainPassword = "RootAdmin"

inputPassword = input("\nPlease Enter Your Password --> ")

while inputPassword != mainPassword:
    tries -= 1

    print(f"\nWrong Password, { 'Last' if tries == 0 else tries } Chance Left")

    inputPassword = input("\nPlease Enter Your Password --> ")

    if tries == 0:
        print("\nAll Tries Is Finished")
        break

else:
    print("\nCorrect Password")
