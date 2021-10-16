import sqlite3

# TODO: utilizar restrições de integridade
con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS user (username TEXT, password TEXT, email TEXT)')
con.commit()

# get user entry
def get_user_by_name(username):
    return cur.execute(f'SELECT * FROM user WHERE username=?',(username,)).fetchone()

def get_user_by_email(email):
    return cur.execute(f'SELECT * FROM user WHERE email=?', (email,)).fetchone()

# insert user entry
def insert_user(user):
    cur.execute('INSERT INTO user VALUES (?, ?, ?)', (user.name, user.password, user.email))
    con.commit()

# close the database connection
def close():
    con.close()
