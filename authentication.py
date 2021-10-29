import database as db


def create_account(username, password, email):
    ''' Criação da conta de usuário.

    Parâmetros:
    - username: nome da conta do usuário
    - password: senha do usuário (sim, não é seguro)
    - email: e-mail do usuário
    
    Retornos:
    - 1: nome de usuário já cadastrado
    - 2: email de usuário já cadastrado
    - 0 / None: criação realizada com sucesso '''
    if db.get_user_by_name(username): return 1
    if db.get_user_by_email(email): return 2 
    db.insert_user(username, password, email)
    return 0

# TODO: refatorar.
# log user in
# def login(self):
#     user_data = db.get_user_by_name(self.name)
#     if not user_data:
#         print('Usuário não encontrado')
#         return 1
#     password = user_data[1]
#     if self.password != password:
#         print('Senha inválida')
#         return 1
#     print('Login realizado')
#     return 0
