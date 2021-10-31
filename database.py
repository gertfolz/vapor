''' Gerenciador do banco da dados. '''
import sqlite3


# TODO: utilizar restrições de integridade?
# TODO: criar um script separado só pra isso, de modo que essa inicialização não
#     seja realizada sempre que o software é executado?
# Inicialização do banco de dados.
con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS user (username TEXT, password TEXT, \
    email TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS friendship (username1 TEXT, \
    username2 TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS user_game (username TEXT, game TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS game (name TEXT, price_buy TEXT, \
    price_rent TEXT, desc TEXT, release_date TEXT, developer TEXT)')
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

def insert_friendship(username1: str, username2: str):
    ''' Insere uma nova entrada de amizade entre usuários. '''
    cmd = 'INSERT INTO friendship VALUES (?, ?)'
    cur.execute(cmd, (username1, username2))
    con.commit()

def insert_user_game(username: str, game_name: str):
    ''' Insere um novo jogo à lista de jogos do usuário. '''
    cmd = 'INSERT INTO user_game VALUES (?, ?)'
    cur.execute(cmd, (username, game_name))
    con.commit()

def insert_game(game: object):
    '''Insere um novo jogo à lista de jogos na loja. '''
    cmd = 'INSERT INTO game VALUES (?, ?, ?, ?, ?, ?)'
    cur.execute(cmd, (game.name, game.price_buy, game.price_rent, game.desc, \
        game.release_date, game.developer))
    con.commit()


# TODO: abrir e fechar antes e depois de cada operação?
def close():
    ''' Fecha a conexão do banco de dados. '''
    con.close()
