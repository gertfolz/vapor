''' Módulo utilizado para testes diretamente no terminal. '''
import authentication as auth
import database as db


OPTIONS = '012'
MENU = '1 - Criar conta\n2 - Login\n0 - Sair\n'
CREATION_CODES = {1: 'Nome de usuário já existente',
                  2: 'E-mail já cadastrado'}

# def get_login_data():
#     username = input('\nUsuário: ')
#     password = input('Senha: ')

def get_account_creation_data():
    username = input('\nUsuário: ')
    password = input('Senha: ')
    email = input('E-mail: ')
    return (username, password, email)


if __name__ == '__main__':

    # leitura da opção
    option = input(MENU)
    while option not in OPTIONS:
        option = input(MENU)

    # TODO: utilizar um dict de funções para executar os opções?
    # execução da opção
    if option == '1':
        data = get_account_creation_data()
        cod = auth.create_account(data[0], data[1], data[2])
        while (cod != 0):
            print(CREATION_CODES[cod])
            data = get_account_creation_data()
            cod = auth.create_account(data[0], data[1], data[2])

    # elif option == '2':
    #     data = get_login_data()
    #     while (user.login() != 0):
    #         get_login_data()

    # TODO: remover o fechamento caso ele seja retirado do módulo do banco.
    elif option == '0':
        db.close()
        exit(0)
