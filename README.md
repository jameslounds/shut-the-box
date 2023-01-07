# Shut the Box

This is a simple implementation of shut the box in python.
You can only flip down numbers, if you rolled an 8, and had only a 9 left, you cannot flip up 9, and flip down 1.
The player's pieces are stored as a bitfield, where a 1 represents a number that is flipped down.
The `main.py` script runs an infinite loop, playing a turn each iteration. If the game has been won, the loop is broken, and the winner is announced.

# Player's choose_move function

The goal of this repo is not to write an AI to play this game, so the AI is incredibly simple, and fairly inefficient.
We loop over the available numbers. If we can match the roll in one move, we do. If not, we try for two moves, and so on to four moves. No roll can be made by flipping more than 4 pieces down.
