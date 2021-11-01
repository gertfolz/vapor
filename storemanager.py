'''
Módulo que contém funções associadas à gerência da loja da plataforma.
'''
import database as db
from game import Game

def get_games():
    ''' Recupera uma lista com os nomes de todos os jogos presentes na loja. '''
    return list(zip(*db.get_games()))[0]

def initialize_games():
    ''' Inicializa a loja com jogos lidos de um arquivo texto.
    É uma função utilizada apenas para a realização de testes, atualmente. '''
    game = Game()
    with open('./games/games.txt', encoding='utf-8') as f:
        while True:
            # Leitura dos dados.
            game.name = f.readline().rstrip()
            if not game.name: break
            game.price_buy = f.readline().rstrip()
            game.price_rent = f.readline().rstrip()
            game.desc = f.readline().rstrip()
            game.release_date = f.readline().rstrip()
            game.developer = f.readline().rstrip()
            f.readline() # joga a linha em branco fora
            
            # Adição no banco de dados caso não exista.
            if not db.get_game_by_name(game.name): db.insert_game(game)

# TODO: remover após implementar a compra de jogos.
def initialize_library():
    ''' Inicializa uma biblioteca de jogos para teste. '''
    if not db.get_user_game('a', 'Celeste'):
        db.insert_user_game('a', 'Celeste', 0) # zero indica jogo comprado
    if not db.get_user_game('a', 'The Witcher 3: Wild Hunt'):
        db.insert_user_game('a', 'The Witcher 3: Wild Hunt', 1)
    if not db.get_user_game('a', 'The Elder Scrolls V: Skyrim'):
        db.insert_user_game('a', 'The Elder Scrolls V: Skyrim', 0)

''' ------------------------------------------------------------------------ '''

''' Testes. '''
if __name__ == '__main__':
    import sys
    import misc

    # Inicialização dos jogos.
    misc.separator('STORE MANAGER: INICIALIZAÇÃO DOS JOGOS')
    initialize_games()

    # Leitura de todos os jogos.
    misc.separator('STORE MANAGER: LEITURA DOS JOGOS')
    get_games()

    sys.exit(0)
