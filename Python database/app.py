import os, sqlite3

os.chdir(os.path.dirname(os.path.abspath(__file__)))

dbConnect = sqlite3.connect('app.db')
dbCursor = dbConnect.cursor()

# dbCursor.execute(
#     '''
#     create table if not exists users (
#         user_id integer primary key autoincrement,
#         name text
#     );
#     '''
# )

# dbCursor.execute(
#     '''
#     create table if not exists skills (
#         skill_id integer primary key autoincrement,
#         name text,
#         progress integer,
#         user_id integer
#     );
#     '''
# )

# my_users = ['root', 'admin', 'manager', 'ahmed', 'omer', 'ali', 'gamal', 'mohammed']
# for user in my_users:
#     dbCursor.execute(f'insert into users(name) values("{user}");')

# dbCursor.execute('update users set name = "Admin User" where user_id = 4;')
# dbCursor.execute('update users set name = "Manager User" where user_id = 5;')
# dbCursor.execute('update users set name = "Super User" where user_id = 6;')
# dbCursor.execute('update users set name = "Power User" where user_id = 7;')
# dbCursor.execute('update users set name = "Root User" where user_id = 8;')

# dbCursor.execute('delete from users where user_id between 9 and 28;')

dbCursor.execute('select * from users;')

print(dbCursor.fetchall())

dbConnect.commit()

dbConnect.close()
