import db

class User:
    def __init__ (self):
        self.name = None
        self.password = None
        self.email = None

    # print user info
    def print_user(self):
        print(f'{self.name}\n{self.password}\n{self.email}')
    
    # create user account
    def create_account(self):
        user_data = db.get_user_by_name(self.name)
        if user_data:
            print('Nome de usuário já existe')
            return 1
        user_data = db.get_user_by_email(self.email)
        if user_data:
            print('Email já utilizado')
            return 1
        db.insert_user(self)
        print('Conta criada')
        return 0

    # log user in
    def login(self):
        user_data = db.get_user_by_name(self.name)
        if not user_data:
            print('Usuário não encontrado')
            return 1
        password = user_data[1]
        if self.password != password:
            print('Senha inválida')
            return 1
        print('Login realizado')
        return 0
