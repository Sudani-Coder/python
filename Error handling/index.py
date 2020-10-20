the_file = None
the_tries = 5

while the_tries > 0:
    try:
        print("Enter the file name with absolute path to open")
        print(f"You have {the_tries} tries left")
        print(r"Example: C:\Users\SudaniCoder\Desktop")

        file_path = input("File name => ").strip()

        the_file = open(file_path, "r")

        print(the_file.read())

        break

    except FileNotFoundError:
        print("File error, file not found please be sure the file path is valid")
        the_tries -= 1

    except:
        print("File error!")

    finally:
        if the_file is not None:
            the_file.close()
            print("File Closed.")

else:
    print("All tries is done")
