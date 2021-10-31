from dataclasses import dataclass

@dataclass
class User:
    ''' Classe que representa um usuário.
    Utilizada para manter o estado do usuário que está utilizando o sistema. '''
    username: str = None # nome de usuário
    password: str = None # senha do usuário
    email: str = None # e-mail do usuário
