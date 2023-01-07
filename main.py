from player import Player
from game import Game

players = [Player(), Player(), Player(), Player()]
game = Game(players)
game.drawBoard()
while True:
    winner = game.doTurn()
    if winner:
        print("No players can move, game over")
        print("Winner is player", winner)
        break
    game.drawBoard()
