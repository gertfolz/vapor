from dataclasses import dataclass


@dataclass
class Game:
    ''' Classe que representa um jogo.
    É utilizada para facilitar a passagem de dados entre módulos. '''
    name: str = None # nome do jogo
    price_buy: float = None # preço de compra do jogo
    price_rent: float = None # preço de aluguel do jogo
    desc: str = None # descrição do jogo
    release_date: str = None # data de lançamento do jogo
    developer: str = None # desenvolvedor do jogo

