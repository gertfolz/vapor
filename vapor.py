from user import User
import db


OPTIONS = '012'
MENU = '1 - Login\n2 - Criar conta\n0 - Sair\n'
user = User()

def get_login_data():
    user.name = input('\nUsuário: ')
    user.password = input('Senha: ')

def get_account_creation_data():
    user.name = input('\nUsuário: ')
    user.password = input('Senha: ')
    user.email = input('E-mail: ')


if __name__ == '__main__':

    # get option'
    option = input(MENU)
    while option not in OPTIONS:
        option = input(MENU)

    # execute option
    if option == '1':
        get_login_data()
        while (user.login() != 0):
            get_login_data()

    elif option == '2':
        get_account_creation_data()
        while (user.create_account() != 0):
            get_account_creation_data()

    elif option == '0':
        db.close()
        exit(0)
