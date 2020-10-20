# List contains admins
admins = ["admin", "root", "manager", "superuser"]

while True:
    # Login
    name = input("Please Type Your Name --> ").strip().lower()

    # If name is in admin
    if name in admins:
        print(f"hello {name} welcome back.")
        option = input("Delete Or Update Your Name ? ").strip().lower()

        # update option
        if option == "update" or option == "u":
            theNewName = input("Please Type Your New Name --> ").strip().lower()
            admins[admins.index(name)] = theNewName
            print("Name Updated.")
            print(admins)

        # delete option
        elif option == "delete" or option == "d":
            admins.remove(name)
            print("Name Deleted.")
            print(admins)
        
        else:
            print("Wrong Option.")

    elif name not in admins:
        print("Your Are Not Admin.")
        status = input("Not Admin, Add You Yes(Y), No(N) ? ").strip().lower()
        if status == "yes" or status == "y":
            print("You Have Been Added.")
            admins.append(name)
            print(admins)
        
        elif status == "no" or status == "n":
            print("You Are Not Added.")
            exit(0)
        
        else:
            print("Wrong Input.")
