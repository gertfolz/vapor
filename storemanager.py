'''
Módulo que contém funções associadas à gerência da loja da plataforma.
'''
import database as db
from game import Game


def initialize_games():
    ''' Inicializa a loja com jogos lidos de um arquivo texto.
    É uma função utilizada apenas para a realização de testes. '''
    new_game = Game()
    with open('./games/games.txt', encoding='utf-8') as f:
        while True:
            new_game.name = f.readline().rstrip()
            if not new_game.name: break
            new_game.price_buy = f.readline().rstrip()
            new_game.price_rent = f.readline().rstrip()
            new_game.desc = f.readline().rstrip()
            new_game.release_date = f.readline().rstrip()
            new_game.developer = f.readline().rstrip()
            f.readline() # joga a linha em branco fora
            print(new_game, end='\n\n')
            db.insert_game(new_game)

''' ------------------------------------------------------------------------ '''

''' Testes. '''
if __name__ == '__main__':
    import misc


    # Inicialização dos jogos.
    misc.separator('INICIALIZAÇÃO DOS JOGOS')
    initialize_games()
