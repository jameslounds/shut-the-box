from random import randint
from player import Player, bit_field_to_num


class Game:
    def __init__(self, players: Player):
        self.players = players
        self.current_player = 0
        self.winner = None

    def doTurn(self):
        if (all([player.isOut for player in self.players])):
            scores = [sum(bit_field_to_num(self.players[player].pieces))
                      for player in range(len(self.players))]
            self.winner = scores.index(min(scores))
            return self.winner

        if not self.players[self.current_player].isOut:
            roll = randint(1, 6) + randint(1, 6)
            print(f"{self.current_player} rolled a {roll}")
            chosen_move = self.players[self.current_player].choose_move(roll)
            if chosen_move == 0:
                print("they're out, with a score of", sum(
                    bit_field_to_num(self.players[self.current_player].pieces)))
            else:
                print("they're flipping",  bit_field_to_num(~chosen_move))
            self.players[self.current_player].pieces = self.players[self.current_player].pieces ^ chosen_move
        self.current_player = (self.current_player + 1) % len(self.players)

    def drawBoard(self):
        print(f"""
                  │ {"9" if not self.players[2].pieces & 1 << 8 else " "}  {"8" if not self.players[2].pieces & 1 << 7 else " "}  {"7" if not self.players[2].pieces & 1 << 6 else " "}  {"6" if not self.players[2].pieces & 1 << 5 else " "}  {"5" if not self.players[2].pieces & 1 << 4 else " "}  {"4" if not self.players[2].pieces & 1 << 3 else " "}  {"3" if not self.players[2].pieces & 1 << 2 else " "}  {"2" if not self.players[2].pieces & 1 << 1 else " "}  {"1" if not self.players[2].pieces & 1 else " "} │
                ─ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ ─
                {"1" if not self.players[1].pieces & 1 << 0 else " "} ┃                           ┃ {"9" if not self.players[3].pieces & 1 << 8 else " "}
                {"2" if not self.players[1].pieces & 1 << 1 else " "} ┃                           ┃ {"8" if not self.players[3].pieces & 1 << 7 else " "}
                {"3" if not self.players[1].pieces & 1 << 2 else " "} ┃                           ┃ {"7" if not self.players[3].pieces & 1 << 6 else " "}
                {"4" if not self.players[1].pieces & 1 << 3 else " "} ┃                           ┃ {"6" if not self.players[3].pieces & 1 << 5 else " "}
                {"5" if not self.players[1].pieces & 1 << 4 else " "} ┃                           ┃ {"5" if not self.players[3].pieces & 1 << 4 else " "}
                {"6" if not self.players[1].pieces & 1 << 5 else " "} ┃                           ┃ {"4" if not self.players[3].pieces & 1 << 3 else " "}
                {"7" if not self.players[1].pieces & 1 << 6 else " "} ┃                           ┃ {"3" if not self.players[3].pieces & 1 << 2 else " "}
                {"8" if not self.players[1].pieces & 1 << 7 else " "} ┃                           ┃ {"2" if not self.players[3].pieces & 1 << 1 else " "}
                {"9" if not self.players[1].pieces & 1 << 8 else " "} ┃                           ┃ {"1" if not self.players[3].pieces & 1 << 0 else " "}
                ─ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ ─
                  │ {"1" if not self.players[0].pieces & 1 << 0 else " "}  {"2" if not self.players[0].pieces & 1 << 1 else " "}  {"3" if not self.players[0].pieces & 1 << 1 else " "}  {"4" if not self.players[0].pieces & 1 << 3 else " "}  {"5" if not self.players[0].pieces & 1 << 4 else " "}  {"6" if not self.players[0].pieces & 1 << 5 else " "}  {"7" if not self.players[0].pieces & 1 << 6 else " "}  {"8" if not self.players[0].pieces & 1 << 7 else " "}  {"9" if not self.players[0].pieces & 8 else " "} │
              """
              )
