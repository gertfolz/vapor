'''
Módulo utilizado para a realização de testes diretamente no terminal.
'''
import sys
import misc
import authentication as auth
import database as db
import storemanager as sm
import librarymanager as lm
from user import User

INITIAL_MENU_OPTIONS = '012'
LIBRARY_MENU_OPTIONS = '01'
STORE_MENU_OPTIONS =   '012'

INITIAL_MENU = '[1] Criar conta\n[2] Login\n[0] Sair\n'
LIBRARY_MENU = '\n[1] Loja de Jogos\n[0] Sair\n'
STORE_MENU =   '\n[1] Pesquisar Jogo\n[2] Biblioteca de Jogos\n[0] Sair\n'

CREATION_CODES =  { 1: 'Nome de usuário já existente',
                    2: 'E-mail já cadastrado' }
LOGIN_CODES =     { 1: 'Usuário não encontrado',
                    2: 'Senha incorreta' }
GAME_MODE_CODES = { 0: 'Comprado',
                    1: 'Alugado' }

user = User()

def get_initial_menu_option():
    ''' Menu inicial do sistema. '''
    misc.separator('VAPOR')
    return input(INITIAL_MENU)

def get_login_data():
    ''' Formulário de login de usuário. '''
    misc.separator('VAPOR: LOGIN')
    user.username = input('Usuário: ')
    user.password = input('Senha: ')

def get_account_creation_data():
    ''' Formulário de criação de conta de usuário. '''
    misc.separator('VAPOR: CRIAÇÃO DE CONTA')
    user.username = input('Usuário: ')
    user.password = input('Senha: ')
    user.email = input('E-mail: ')

def show_user_library():
    ''' Mostra a biblioteca de jogos do usuário. '''
    misc.separator(f'VAPOR: BIBLIOTECA DE JOGOS -- {user.username}')
    for game in lm.get_user_library(user.username):
        print(f'{game[0]} [{GAME_MODE_CODES[game[1]]}]')

def get_library_menu_option():
    ''' Menu mostrado na biblioteca de jogos do usuário. '''
    return input(LIBRARY_MENU)

def show_game_store():
    misc.separator(f'VAPOR: LOJA DE JOGOS -- {user.username}')
    for game in sm.get_games(): print(game)

def get_store_menu_options():
    ''' Menu mostrado na loja de jogos. '''
    return input(STORE_MENU)

''' ------------------------------------------------------------------------ '''

''' Execução do sistema através de uma interface de usuário no terminal. '''
if __name__ == '__main__':
    # Inicialização do banco de dados para teste.
    auth.initialize_users()
    sm.initialize_games()
    sm.initialize_library()

    ''' Menu inicial ------------------------------------------------------- '''

    # leitura da opção
    option = get_initial_menu_option()
    while option not in INITIAL_MENU_OPTIONS:
        option = get_initial_menu_option()

    # TODO: utilizar um dict de funções para executar os opções?
    # execução da opção de criação de conta de usuário
    if option == '1':
        get_account_creation_data()
        cod = auth.create_account(user)
        while cod != 0:
            print(CREATION_CODES[cod])
            get_account_creation_data()
            cod = auth.create_account(user)

    # execução da opção de login de usuário
    elif option == '2':
        get_login_data()
        cod = auth.login(user)
        while cod != 0:
            print(LOGIN_CODES[cod])
            get_login_data()
            cod = auth.login(user)

    # TODO: remover o fechamento caso ele seja retirado do módulo do banco.
    elif option == '0':
        db.close()
        sys.exit(0)

    ''' Biblioteca do usuário ---------------------------------------------- '''

    show_user_library() # TODO: remover após implementar a compra de jogos
    option = get_library_menu_option()
    while option not in LIBRARY_MENU_OPTIONS:
        show_user_library()
        option = get_library_menu_option()

    if option == '0':
        db.close()
        sys.exit(0)
    
    ''' Página da loja ----------------------------------------------------- '''
    
    show_game_store()
    option = get_store_menu_options()
    while option not in STORE_MENU_OPTIONS:
        show_game_store()
        option = get_store_menu_options()
    
    if option == '1': # TODO: implementar a pesquisa de jogos
        pass

    elif option == '2':
        show_user_library()
    
    elif option == '0':
        db.close()
        sys.exit(0)

    db.close()
    sys.exit(0)
