'''
Módulo que contém funções associadas à gerência da loja da plataforma.
'''
import database as db
from game import Game

def initialize_games(verbose: bool = False):
    ''' Inicializa a loja com jogos lidos de um arquivo texto.
    É uma função utilizada apenas para a realização de testes. '''
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
            if verbose: print(game, end='\n\n')
            if not db.get_game_by_name(game.name): db.insert_game(game)

''' ------------------------------------------------------------------------ '''

''' Testes. '''
if __name__ == '__main__':
    import sys
    import misc

    # Inicialização dos jogos.
    misc.separator('INICIALIZAÇÃO DOS JOGOS')
    initialize_games(verbose=True)

    sys.exit(0)
