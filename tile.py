'''a single tile in the Othello board'''
class Tile():

    #the three states a tile can be in
    BLANK = 'blank'
    RED = 'red'
    BLACK = 'black'

    def __init__(self, *args, **kwargs):
        self.status = self.BLANK

    def print_status(self):
        print(self.status, end=' | ')
