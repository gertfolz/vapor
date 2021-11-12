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

def get_friendship(sender: str, receiver: str):
    ''' Recupera uma entrada de amizade entre dois usuários. '''
    cmd = 'SELECT * FROM friendship WHERE sender=? AND receiver=?'
    return cur.execute(cmd, (sender, receiver)).fetchone()

def get_friendship_by_sender(sender: str):
    ''' Recupera uma entrada de amizade entre dois usuários pelo remetente. '''
    cmd = 'SELECT * FROM friendship WHERE sender=?'
    return cur.execute(cmd, (sender,)).fetchone()

def get_friendship_by_receiver(receiver: str):
    ''' Recupera uma entrada de amizade entre dois usuários pelo recebedor. '''
    cmd = 'SELECT * FROM friendship WHERE receiver=?'
    return cur.execute(cmd, (receiver,)).fetchone()

def get_friendships(username: str):
    ''' Recupera as amizades nas quais o usuário participa. '''
    cmd1 = 'SELECT sender, receiver FROM friendship WHERE sender=?'
    cmd2 = 'SELECT sender, receiver FROM friendship WHERE receiver=?'
    return cur.execute(f'{cmd1} UNION {cmd2}', (username, username)).fetchall()

def get_pending_friendship_requests(receiver: str):
    ''' Recupera os pedidos pendentes enviados para o recebedor. '''
    cmd = '''SELECT sender, receiver FROM friendship WHERE receiver=? 
        AND pending=?'''
    return cur.execute(cmd, (receiver, 1)).fetchall()

def insert_friendship_request(sender: str, receiver: str):
    ''' Insere uma nova entrada de amizade pendente entre usuários. '''
    cmd = 'INSERT INTO friendship VALUES (?, ?, ?)'
    cur.execute(cmd, (sender, receiver, 1))
    con.commit()

def accept_friendship_request(sender: str, receiver: str):
    ''' Atualiza uma entrada de amizade existente para não pendente. '''
    cmd = 'UPDATE friendship SET pending = 0 WHERE sender=? AND receiver=?'
    cur.execute(cmd, (sender, receiver))
    con.commit()

def reject_friendship_request(sender: str, receiver: str):
    ''' Rejeita (deleta) um pedido de amizade pendente. '''
    cmd = 'DELETE FROM friendship WHERE sender=? AND receiver=?'
    cur.execute(cmd, (sender, receiver))
    con.commit()

''' User game library ------------------------------------------------------ '''

def insert_user_game(username: str, game_name: str, rented: int, timestamp: object = None):
    ''' Insere um novo jogo à lista de jogos do usuário. '''
    cmd = 'INSERT INTO user_game VALUES (?, ?, ?, ?)'
    cur.execute(cmd, (username, game_name, rented, timestamp))
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
        sender TEXT NOT NULL,
        receiver TEXT NOT NULL,
        pending INTEGER NOT NULL,
        PRIMARY KEY(sender, receiver),
        FOREIGN KEY(sender) REFERENCES user(username),
        FOREIGN KEY(receiver) REFERENCES user(username))''')

    # Jogos adquiridos ou alugados por cada usuário.
    cur.execute('''CREATE TABLE IF NOT EXISTS user_game (
        username TEXT NOT NULL,
        game_name TEXT NOT NULL,
        rented INTEGER NOT NULL,
        timestamp INTEGER,
        PRIMARY KEY(username, game_name),
        FOREIGN KEY(username) REFERENCES user(username),
        FOREIGN KEY(game_name) REFERENCES game(name))''')

    con.commit()
    con.close()
    sys.exit(0)
