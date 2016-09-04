import tkinter as tk

class Board(tk.TK):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.board = tk.Frame(self)
        self.board.grid()

        self.squares = []

    def create_squares:

        for x in range(8):
            self.squares.append([])
            for y in range(8):
                self.squares[x].append(tk.Frame(self.board))
                self.squares[x][y].grid(row=x, column=y)


