'''
Gerenciador do banco da dados.
'''
import sqlite3

# TODO: utilizar restrições de integridade?
# TODO: criar um script separado só pra isso, de modo que essa inicialização não
#     seja realizada sempre que o software é executado?
con = sqlite3.connect('database.db')
cur = con.cursor()

''' User ------------------------------------------------------------------- '''

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

''' Game ------------------------------------------------------------------- '''

def insert_game(game: object):
    ''' Insere um novo jogo à lista de jogos na loja. '''
    cmd = 'INSERT INTO game VALUES (?, ?, ?, ?, ?, ?)'
    cur.execute(cmd, (game.name, game.price_buy, game.price_rent, game.desc, \
        game.release_date, game.developer))
    con.commit()

def get_game_by_name(game_name: str):
    ''' Recupera os dados de um jogo pelo nome. '''
    cmd = 'SELECT * FROM game where name=?'
    return cur.execute(cmd, (game_name,)).fetchone()

def get_games():
    ''' Recupera todos os jogos cadastrados no sistema. '''
    cmd = 'SELECT * FROM game'
    return cur.execute(cmd, ()).fetchall()

''' Friendship ------------------------------------------------------------- '''

def insert_friendship(username1: str, username2: str):
    ''' Insere uma nova entrada de amizade entre usuários. '''
    cmd = 'INSERT INTO friendship VALUES (?, ?)'
    cur.execute(cmd, (username1, username2))
    con.commit()

''' User game library ------------------------------------------------------ '''

def insert_user_game(username: str, game_name: str, rented: int):
    ''' Insere um novo jogo à lista de jogos do usuário. '''
    cmd = 'INSERT INTO user_game VALUES (?, ?, ?)'
    cur.execute(cmd, (username, game_name, rented))
    con.commit()

def get_user_game(username: str, game_name: str):
    ''' Recupera um jogo da biblioteca do usuário. '''
    cmd = 'SELECT * FROM user_game WHERE username=? AND game_name=?'
    return cur.execute(cmd, (username, game_name)).fetchone()

def get_user_games(username: str):
    ''' Recupera todos os jogos associados ao usuário. '''
    cmd = 'SELECT game_name, rented FROM user_game WHERE username=?'
    return cur.execute(cmd, (username,)).fetchall()

''' ------------------------------------------------------------------------ '''

# TODO: abrir e fechar antes e depois de cada operação?
def close():
    ''' Fecha a conexão do banco de dados. '''
    con.close()

''' ------------------------------------------------------------------------ '''

''' Inicialização do banco de dados, separado do resto do módulo para não ser
executado a cada execução do sistema. '''
if __name__ == '__main__':
    import sys

    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute('''DROP TABLE IF EXISTS user''')
    cur.execute('''DROP TABLE IF EXISTS game''')
    cur.execute('''DROP TABLE IF EXISTS friendship''')
    cur.execute('''DROP TABLE IF EXISTS user_game''')

    # Dados de cada usuário.
    cur.execute('''CREATE TABLE IF NOT EXISTS user (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        email TEXT NOT NULL)''')

    # Dados de cada jogo.
    cur.execute('''CREATE TABLE IF NOT EXISTS game (
        name TEXT PRIMARY KEY,
        price_buy TEXT NOT NULL,
        price_rent TEXT,
        desc TEXT NOT NULL,
        release_date TEXT NOT NULL,
        developer TEXT NOT NULL)''')

    # Amizades entre os usuários.
    cur.execute('''CREATE TABLE IF NOT EXISTS friendship (
        username1 TEXT NOT NULL,
        username2 TEXT NOT NULL,
        PRIMARY KEY(username1, username2),
        FOREIGN KEY(username1) REFERENCES user(username),
        FOREIGN KEY(username2) REFERENCES user(username))''')

    # Jogos adquiridos ou alugados por cada usuário.
    cur.execute('''CREATE TABLE IF NOT EXISTS user_game (
        username TEXT NOT NULL,
        game_name TEXT NOT NULL,
        rented INTEGER NOT NULL,
        PRIMARY KEY(username, game_name),
        FOREIGN KEY(username) REFERENCES user(username),
        FOREIGN KEY(game_name) REFERENCES game(name))''')

    con.commit()
    con.close()
    sys.exit(0)
