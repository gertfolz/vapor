import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS user (username TEXT, password TEXT)")
con.commit()

def getUser(username):
    return cur.execute(f"SELECT * FROM user WHERE username=?",(username,)).fetchall()

def insertUser(user):
    cur.execute("INSERT INTO user VALUES (?, ?)", (user.name, user.password))
    con.commit()


