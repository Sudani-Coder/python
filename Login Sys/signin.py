import getpass, hashlib, sqlite3
from sqlite3 import Error

def login():
    text = """
    ##################################################
    #                                                #
    #         Hello World To My Login System         #
    #    ========================================    #
    #    1.Create New Account.                       #
    #    2.Login To An Existing Account.             #
    #    3.Delete An Existing Account.               #
    #    4.Exit from the system                      #
    #    ========================================    #
    #                                                #
    #    Please Select A Number From The Menu :-)    #
    #                                                #
    ##################################################
    """
    print(text)
    try:
        choice = int(input(" Please Enter The Number --> "))
        if choice == 1:
            username = hashlib.md5(input("\n Please Enter User Name --> ").encode(encoding="utf-8")).hexdigest()
            password = hashlib.md5(getpass.getpass(prompt="\n Please Enter The Password --> ").encode(encoding="utf-8")).hexdigest()
            repassword = hashlib.md5(getpass.getpass(prompt="\n Please Confirm your Password --> ").encode(encoding="utf-8")).hexdigest()
            if password == repassword:
                """ create a database connection to a SQLite database """
                try:
                    connection = sqlite3.connect("users.db")
                    curconnsor = connection.cursor()
                    curconnsor.execute(
                        """
                        CREATE TABLE IF NOT EXISTS users (
                            ID integer PRIMARY KEY AUTOINCREMENT,
                            UserName text NOT NULL,
                            PassWord text NOT NULL
                        );
                        """
                    )
                    curconnsor.execute("INSERT INTO users(UserName, PassWord) VALUES(?, ?);", (username, password))
                except Error as e:
                    print(e)
                
                finally:
                    if connection:
                        connection.commit()
                        connection.close()

                print("\n your account is created successfully!\n")
            else:
                print("\n\a\a Error -> Password does not match!\a\a\n")
        elif choice == 2:
            print("\n cooming soon\n")
        elif choice == 3:
            print("\n cooming soon\n")
        elif choice == 4:
            exit(0)
        else:
            print("\n\a\a Value Error -> Out of Range -> Please Enter A Valid Number!\a\a\n")
    except ValueError:
        print("\n\a\a Value Error -> Invalid Input(Data Type) -> Please Enter A Number(integer) Only!\a\a\n")

def main():
    while True:
        login()

if __name__ == "__main__":
    main()
