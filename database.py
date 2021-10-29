import sqlite3

# TODO: utilizar restrições de integridade?
con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS user (username TEXT, password TEXT, email TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS friendship (username1 TEXT, username2 TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS userGames (username TEXT, game TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS game (name TEXT, priceBuy TEXT, priceRent TEXT, desc TEXT, releaseDate TEXT, developer TEXT)')
con.commit()

def get_user_by_name(username):
    ''' Recupera os dados de um usuário pelo nome de usuário. '''
    cmd = 'SELECT * FROM user WHERE username=?'
    return cur.execute(cmd, (username,)).fetchone()

def get_user_by_email(email):
    ''' Recupera os dados de um usuário pelo e-mail '''
    cmd = 'SELECT * FROM user WHERE email=?'
    return cur.execute(cmd, (email,)).fetchone()

def insert_user(username, password, email):
    ''' Insere uma nova entrada de usuário. '''
    cmd = 'INSERT INTO user VALUES (?, ?, ?)'
    cur.execute(cmd, (username, password, email))
    con.commit()

def insert_friendship(username1, username2):
    ''' Insere uma nova entrada de amizade entre usuários. '''
    cmd = 'INSERT INTO friendship VALUES (?, ?)'
    cur.execute(cmd, (username1, username2))
    con.commit()

def insert_gameToUserLibrary(username, game):
    ''' Insere um novo jogo à lista de jogos do usuário. '''
    cmd = 'INSERT INTO userGames VALUES (?, ?)'
    cur.execute(cmd, (username, game))
    con.commit()

def insert_game(game):
    '''Insere um novo jogo à lista de jogos na loja. '''
    cmd = 'INSERT INTO game VALUES (?, ?, ?, ?, ?, ?)'
    cur.execute(cmd, (game.name, game.priceBuy, game.priceRent, game.desc, game.releaseDate, game.developer))
    con.commit()




# TODO: abrir e fechar antes e depois de cada operação?
def close():
    ''' Fecha a conexão do banco de dados. '''
    con.close()
