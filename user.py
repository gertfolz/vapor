''' Classe que representa um usuário.
É utilizada para manter o estado do usuário que está utilizando o sistema. '''
from dataclasses import dataclass


@dataclass
class User:
    username: str = None # nome de usuário
    password: str = None # senha do usuário
    email: str = None # e-mail do usuário
