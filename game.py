''' Classe que representa um jogo. '''
from dataclasses import dataclass


@dataclass
class Game:
    name: str = None # nome do jogo
    priceBuy: float = None # preço de compra do jogo
    priceRent: float = None # preço de aluguel do jogo
    desc: str = None # descrição do jogo
    releaseDate: str = None # data de lançamento do jogo
    developer: str = None # desenvolvedor do jogo

