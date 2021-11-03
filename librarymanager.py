'''
Módulo que contém funções associadas à gerência de bibliotecas de usuários.
'''
import sys
import database as db

def get_user_library(username: str):
    ''' Recupera a biblioteca de jogos do usuário.
    
    Parâmetros:
    - username: nome do usuário
    
    Retornos:
    - uma lista de tuplas. O primeiro elemento da tupla contém o nome do
    jogo (str), e o segundo contém a forma com a qual ele foi adquirido (int; 0
    indica que foi comprado, 1 indica que foi alugado). '''
    return db.get_user_games(username)

''' ------------------------------------------------------------------------ '''

''' Testes. '''
if __name__ == '__main__':
    # Obtenção da biblioteca do usuário de testes.
    print(get_user_library('a'))
    sys.exit(0)
