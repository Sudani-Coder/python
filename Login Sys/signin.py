import getpass, hashlib, sqlite3

def login():
    text = """
    ##################################################
    #                                                #
    #         Hello World To My Login System         #
    #    ========================================    #
    #    1.Create New Account.                       #
    #    2.Login To An Existing Account.             #
    #    3.Delete An Existing Account.               #
    #    ========================================    #
    #                                                #
    #    Please Select A Number From The Menu :-)    #
    #                                                #
    ##################################################
    """
    print(text)
    try:
        choice = int(input("Please Enter The Number --> "))
        if choice == 1:
            username = hashlib.md5(input("\nPlease Enter User Name --> ").encode(encoding="utf-8")).hexdigest()
            password = hashlib.md5(getpass.getpass(prompt="\nPlease Enter The Password --> ").encode(encoding="utf-8")).hexdigest()
            repassword = hashlib.md5(getpass.getpass(prompt="\nPlease Confirm your Password --> ").encode(encoding="utf-8")).hexdigest()
            if password == repassword:
                connection = sqlite3.connect("thedb.db")
                curconnsor = connection.cursor()
                print("test")
            else:
                print("\n\a\aError -> Password does not match!\a\a\n")
        elif choice == 2:
            print("2")
        elif choice == 3:
            print("3")
        else:
            print("\n\a\aValue Error -> Out of Range -> Please Enter A Valid Number!\a\a\n")
    except ValueError:
        print("\n\a\aValue Error -> Invalid Input(Data Type) -> Please Enter A Number(integer) Only!\a\a\n")

def main():
    login()

if __name__ == "__main__":
    main()
