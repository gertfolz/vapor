import database as db
from game import Game



def initializeGames():
    newGame = Game()
    with open('./games/games.txt', encoding='utf-8') as f:
        while True:
            newGame.name = f.readline()
            if not newGame.name:
                    break
            newGame.priceBuy = f.readline()
            newGame.priceRent = f.readline()
            newGame.desc = f.readline()
            newGame.releaseDate = f.readline()
            newGame.developer = f.readline()
            db.insert_game(newGame)
