from tile import Tile

'''A board made up of tiles for playing Othello'''
class Board():

    def __init__(self, *args, **kwargs):
        #length and width of board will always be 8
        self.SIZE = 8
        #array that will be filled with arrays
        #containing tiles
        self.board = []

        for row in range(self.SIZE):
            curr_row = []
            for column in range(self.SIZE):
                curr_row.append(Tile())
            self.board.append(curr_row)

    def return_size(self):
        return self.SIZE

    '''prints the tiles in the layout of a SIZExSIZE board'''
    def print_board_status(self):
        print()
        for row in self.board:
            print('| ', end='')
            for square in row:
                square.print_status()
            print('\n')
