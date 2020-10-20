import os, sqlite3

def get_all_data():
    '''
    A function connect to a database and fetch data from the database
    '''
    try:
        # connect to database
        dbConnection = sqlite3.connect('app.db')

        # print success message
        print('connected to database successfully')
        
        # setting up the cursor
        dbCursor = dbConnection.cursor()

        # fetch data from database
        dbCursor.execute('select * from users;')

        # assign data to variable
        results = dbCursor.fetchall()

        # print number of rows
        print(f'database has {len(results)} rows')

        print('showing data:')

        # loop on results
        for user in results:
            print(f'User ID => {user[0]}, Username => {user[1]}')

    except sqlite3.Error as Error:
        print(f'error => {Error}')

    finally:
        if dbConnection:
            # close database connection
            dbConnection.close()
            
            print('connection to database is closed')

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    get_all_data()
