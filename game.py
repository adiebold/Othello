from board import Board

'''A game of Othello'''
class Game():

    def __init__(self, *args, **kwargs):
        self.game_board = Board()

        #human player = true, computer player = false
        self.player_1 = kwargs['player_1']
        self.player_2 = kwargs['player_2']

    '''Gets move from the player'''
    def get_move(self, player):
        if player:
            print()
            row, col = input('Enter the row and column numbers of ' +
            'the tile you would like to claim (ex. "1 2"):\n').split()
            row = int(row)
            col = int(col)
            print(row)
            print(col)
