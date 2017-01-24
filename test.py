from board import Board
from tile import Tile
from game import Game

if __name__ == '__main__':

    new_game = Game(player_1=True, player_2=False)
    new_game.get_move(True)
