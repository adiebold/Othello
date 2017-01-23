from tile import Tile

class Board():

    def __init__(self, *args, **kwargs):
        self.SIZE = 8
        self.board = []

        for row in range(self.SIZE):
            curr_row = []
            for column in range(self.SIZE):
                curr_row.append(Tile())
            self.board.append(curr_row)

    def print_board_status(self):
        print()
        for row in self.board:
            print('| ', end='')
            for square in row:
                square.print_status()
            print('\n')
