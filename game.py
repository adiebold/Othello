from board import Board

'''A game of Othello'''
class Game():

    def __init__(self, *args, **kwargs):
        self.game_board = Board()
        
        #human player = true, computer player = false
        self.player_1 = kwargs['player_1']
        self.player_2 = kwargs['player_2']
