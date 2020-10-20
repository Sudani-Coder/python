import os, sqlite3

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# create new skill operation in the database
def create_skill():
    """
    this function is used to create new skill in the database.
    create new skill operation in the database.
    """
    sk_name = input("Please enter skill name: ").strip().upper()

    # fetch data from database
    dbCursor.execute(f'select name from skills where name = \'{sk_name}\' and user_id = {user_id}')

    # assign data to variable
    skills = dbCursor.fetchone()

    if skills == None: # if theres no skill with this name in database
        print('You can add it')
        sk_prog = input("Please enter skill progress: ").strip()

        dbCursor.execute(
            f'''
            insert into skills(name, progress, user_id) values('{sk_name}', '{sk_prog}', '{user_id}');
            '''
        )
        print("the skill has been created successfully")

    else:
        print('You cannot add it')

# read all skills operation from the database
def read_skills():
    """
    this function is used to read all user skills from the database.
    read all user skills operation from the database.
    """

    # fetch data from database
    dbCursor.execute(f'select * from skills where user_id = {user_id}')

    # assign data to variable
    skills = dbCursor.fetchall()

    # print number of rows
    print(f'you have {len(skills)} skills')

    if len(skills) > 0:
        print('showing skills with progress:')

    # loop on results
    for skill in skills:
        print(f'Skill name => {skill[1]}, Progress => {skill[2]}%')

# update skill operation in the database
def update_skill():
    sk_name = input("Please enter skill name: ").strip().upper()
    sk_prog = input("Please enter skill progress: ").strip()
    dbCursor.execute(f"update skills set progress = '{sk_prog}' where name = '{sk_name}' and user_id = '{user_id}'")
    print("the skill has been updated successfully")

# delete skill operation from the database
def delete_skill():
    sk_name = input("Please enter skill name: ").strip().upper()
    dbCursor.execute(f"delete from skills where name = '{sk_name}' and user_id = '{user_id}'")
    print("the skill has been deleted successfully")

try:
    # connect to database
    dbConnection = sqlite3.connect('app.db')

    # print success message
    print('connected to database successfully')
    
    # setting up the cursor
    dbCursor = dbConnection.cursor()

    # user name input variable
    user_name = input("\nPlease enter your name: ")

    # fetch user data from database
    dbCursor.execute(f"select user_id from users where name = '{user_name}';")

    # save the user_id to a variable
    user_id = dbCursor.fetchone()[0]

    while True:
        # print input message for the user to choose an option from the list
        input_message = """
        What do you want to do ?

            "c" => create new skill
            "r" => read all skills
            "u" => update skill progress
            "d" => delete skill 
            "q" => quit the app

        Choose Option: """

        # input variable to save the option that has been chosen by the user
        user_option = input(input_message).strip().lower()
        print()

        # options list (commands list)
        commands_list = ["c", "r", "u", "d", "q"]

        if user_option in commands_list:
            if user_option == "c":
                create_skill()
            
            elif user_option == "r":
                read_skills()

            elif user_option == "u":
                update_skill()

            elif user_option == "d":
                delete_skill()

            else:
                break
                print("App is closed.")

        else:
            print(f"sorry this command \"{user_option}\" is not found")

except sqlite3.Error as Error:
    print(f'error => {Error}')

except TypeError as Error:
    print(f'error => {Error} => sorry this user "{user_name}" is not found')

finally:
    if dbConnection:
        # save changes to the database
        dbConnection.commit()

        # close database connection
        dbConnection.close()
        
        print('the connection to database is closed')
