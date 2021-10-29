import sqlite3


# TODO: utilizar restrições de integridade?
con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS user (username TEXT, password TEXT, email TEXT)')
con.commit()

def get_user_by_name(username: str):
    ''' Recupera os dados de um usuário pelo nome de usuário. '''
    cmd = 'SELECT * FROM user WHERE username=?'
    return cur.execute(cmd, (username,)).fetchone()

def get_user_by_email(email: str):
    ''' Recupera os dados de um usuário pelo e-mail '''
    cmd = 'SELECT * FROM user WHERE email=?'
    return cur.execute(cmd, (email,)).fetchone()

def insert_user(user: object):
    ''' Insere uma nova entrada de usuário. '''
    cmd = 'INSERT INTO user VALUES (?, ?, ?)'
    cur.execute(cmd, (user.username, user.password, user.email))
    con.commit()

# TODO: abrir e fechar antes e depois de cada operação?
def close():
    ''' Fecha a conexão do banco de dados. '''
    con.close()
