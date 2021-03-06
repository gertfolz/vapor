'''
Módulo que contém funções associadas à gerência da loja da plataforma.
'''
import database as db
from friendshipmanager import get_friends
from game import Game
from datetime import datetime, timedelta

OPTIONS = '123'
CHARACTERS = '/- '

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
    
    if (check_creditCard()):
        return 2
    '''Jogo comprado é inserido na biblioteca do usuário'''
    if not db.get_user_game(user_name, game_name):
        db.insert_user_game(user_name, game_name, 0)
        return 0
    else:
        return 1

def buy_gift(game_name: str, sender:str):
    '''Se o usuário está na lista de amigos do remetente'''

    print(get_friends(sender))
    receiver = input("Nome do destinatário do presente: ")
    
    if (check_creditCard()):
        return 3

    if(receiver in get_friends(sender)):
        if not db.get_user_game(receiver, game_name):
            '''Insere jogo na biblioteca do destinatário e retorna código de sucesso'''
            db.insert_user_game(receiver, game_name, 0)
            return 0
        else:
            '''Destinatário já possui o jogo, retorna o código de erro deste caso'''
            return 1
    else:
        '''Destinatário não está na lista de amigos do remetente, retorna código de erro'''
        return 2

def rent_game(game_name: str, user_name:str):
    
    
    option = input("Selecione por quantos dias deseja alugar:\n 1- 7 dias\n 2- 15 dias\n 3- 30 dias \n")
    while option not in OPTIONS:
        print("Opção inválida!")
        option = input("Selecione por quantos dias deseja alugar o jogo:\n 1- 7 dias\n 2- 15 dias\n 3- 30 dias \n")
    
    if option == '1':
        ts = datetime.now() + timedelta(days=7)
    if option == '2':
        ts = datetime.now() + timedelta(days=15)
    if option == '3':
        ts = datetime.now() + timedelta(days=30)

    if (check_creditCard()):
        return 2

    '''Jogo alugado é inserido na biblioteca do usuário'''
    if not db.get_user_game(user_name, game_name):
        db.insert_user_game(user_name, game_name, 1 , ts)
        return 0
    else:
        return 1
    

def check_creditCard():
    '''Dados do cartão que a gente não vai usar pra nada kk'''

    creditCard = input("Número do cartão de crédito: ")
    creditCard = creditCard.replace(" ", "")
  
    '''Se o número do cartão conter algo além de números ou não ter 16 digitos, retorna erro e a compra será cancelada'''
    if not ((creditCard.isnumeric()) and (len(creditCard) == 16)):
        return 1

    prop = input("Nome do proprietário do cartão: ")

    cvv = input("Código de segurança: ")
    '''Se o código de segurança conter algo além de números ou não ter 3 digitos, retorna erro e a compra será cancelada'''
    if not ((cvv.isnumeric()) and (len(cvv) == 3)):
        return 1

   
    vdate = input("Data de validade: ")
    vdate = vdate.replace("/", "")
    vdate = vdate.replace(" ", "")
    '''Se a data informada conter caracteres que não são digitos, tiver a data de validade expirada ou não possuir 8 digitos, retorna erro e a compra será cancelada'''
    if not ((vdate.isnumeric()) and (len(vdate) == 8)):
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
