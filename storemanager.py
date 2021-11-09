'''
Módulo que contém funções associadas à gerência da loja da plataforma.
'''
import database as db
from friendshipmanager import get_friends
from game import Game

def get_games():
    ''' Recupera uma lista com os nomes de todos os jogos presentes na loja. '''
    return list(zip(*db.get_games()))[0]

def search_game(game_name: str):
    ''' Pesquisa um jogo pelo seu nome.
    
    Parâmetros:
    - game_name: o nome do jogo
    
    Retornos:
    - um objeto contendo os atributos do jogo, ou None'''
    data = db.get_game_by_name(game_name)
    if data:
        game = Game()
        game.name = data[0]
        game.price_buy = data[1]
        game.price_rent = data[2]
        game.desc = data[3]
        game.release_date = data[4]
        game.developer = data[5]
        return game

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

def buy_game(game_name: str, user_name:str):
    
    '''Jogo comprado é inserido na biblioteca do usuário'''
    if not db.get_user_game(user_name, game_name):
        db.insert_user_game(user_name, game_name)
        return 0
    else:
        return 1

def buy_gift(game_name: str, sender:str, receiver:str):

    

    '''Se o usuário está na lista de amigos do remetente'''
    if(receiver in get_friends(sender)):
        if not db.get_user_game(receiver, game_name):
            '''Insere jogo na biblioteca do destinatário e retorna código de sucesso'''
            db.insert_user_game(receiver, game_name)
            return 0
        else:
            '''Destinatário já possui o jogo, retorna o código de erro deste caso'''
            return 1
    else:
        '''Destinatário não está na lista de amigos do remetente, retorna código de erro'''
        return 2

def check_creditCard():
    '''Dados do cartão que a gente não vai usar pra nada kk'''

    creditCard = input("Número do cartão de crédito: ")
    creditCard.strip()
    '''Se o número do cartão conter algo além de números ou não ter 16 digitos, retorna erro e a compra será cancelada'''
    if not ((creditCard.isnumeric()) and (len(creditCard) == 16)):
        print('Número do cartão de crédito inválido')
        return 1
    prop = input("Nome do proprietário do cartão: ")

    cvv = input("Código de segurança: ")
    '''Se o código de segurança conter algo além de números ou não ter 3 digitos, retorna erro e a compra será cancelada'''
    if not ((cvv.isnumeric()) and (len(cvv) == 3)):
        print('Código de segurança inválido')
        return 1

    characters = "/- "
    vdate = input("Data de validade: ")
    vdate.replace(characters, "")
    '''Se a data informada conter caracteres que não são digitos, tiver a data de validade expirada ou não possuir 8 digitos, retorna erro e a compra será cancelada'''
    if not (vdate.isnumeric() == int and len(vdate) == 8 and int(vdate) > 10112021):
        print('Data inválida')
        return 1

    return 0


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
