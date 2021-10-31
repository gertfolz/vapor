''' Módulo utilizado para a realização de testes diretamente no terminal. '''
import sys
import authentication as auth
import database as db
import storemanager as sm
from user import User


OPTIONS = '012'
MENU = '1 - Criar conta\n2 - Login\n0 - Sair\n'
CREATION_CODES = { 1: 'Nome de usuário já existente',
                   2: 'E-mail já cadastrado' }
LOGIN_CODES = { 1: 'Usuário não encontrado',
                2: 'Senha incorreta' }

user = User()

def get_login_data():
    user.username = input('\nUsuário: ')
    user.password = input('Senha: ')

def get_account_creation_data():
    user.username = input('\nUsuário: ')
    user.password = input('Senha: ')
    user.email = input('E-mail: ')

def show_dummy_library():
    print(f'\nUsuário: {user.username}')
    print('Jogos: A, B, C, D, E, F, G')


if __name__ == '__main__':
    # inicialização da loja
    sm.initialize_games()

    # leitura da opção
    option = input(MENU)
    while option not in OPTIONS:
        option = input(MENU)

    # TODO: utilizar um dict de funções para executar os opções?
    # execução da opção de criação de conta de usuário
    if option == '1':
        get_account_creation_data()
        cod = auth.create_account(user)
        while (cod != 0):
            print(CREATION_CODES[cod])
            get_account_creation_data()
            cod = auth.create_account(user)

    # execução da opção de login de usuário
    elif option == '2':
        get_login_data()
        cod = auth.login(user)
        while (cod != 0):
            print(LOGIN_CODES[cod])
            get_login_data()
            cod = auth.login(user)
        show_dummy_library() # TODO: remover após implementar a compra de jogos

    # TODO: remover o fechamento caso ele seja retirado do módulo do banco.
    elif option == '0':
        db.close()
        sys.exit(0)
