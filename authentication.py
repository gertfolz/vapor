import database as db


def create_account(user: object):
    ''' Criação da conta de usuário.

    Parâmetros:
    - username: nome da conta do usuário
    - password: senha do usuário (sim, não é seguro)
    - email: e-mail do usuário
    
    Retornos:
    - 1: nome de usuário já cadastrado
    - 2: email de usuário já cadastrado
    - 0: criação realizada com sucesso '''
    if db.get_user_by_name(user.username): return 1
    if db.get_user_by_email(user.email): return 2 
    db.insert_user(user)
    return 0

def login(user: object):
    ''' Realização da entrada do usuário no sistema.
    
    Parâmetros:
    - username: nome da conta do usuário
    - password: senha do usuário
       
    Retornos:
    - 1: nome de usuário não encontrado
    - 2: senha incorreta
    - 0: entrada realizada com sucesso '''
    data = db.get_user_by_name(user.username)
    if not data: return 1  # uma coleção vazia é considerada falsa
    if user.password != data[1]: return 2
    return 0
