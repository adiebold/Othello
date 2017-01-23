class Tile():

    BLANK = 'blank'
    RED = 'red'
    BLACK = 'black'

    def __init__(self, *args, **kwargs):
        self.status = self.BLANK

    def print_status(self):
        print(self.status, end=' | ')
