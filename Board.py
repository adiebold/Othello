import tkinter as tk

class Board(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.geometry(self, '500x500+150+150')

        self.board = tk.Frame(self, bg = 'blue')
        self.board.pack(side='top', fill='both', expand=True)
        # self.board.pack()

        self.squares = []
        # self.create_squares()

    def create_squares(self):

        for x in range(8):
            self.squares.append([])
            for y in range(8):
                self.squares[x].append(tk.Frame(self.board, bg = 'red'))
                self.squares[x][y].pack(side='top', fill='both', expand=True)
                self.squares[x][y].grid(row=x, column=y)


if __name__ == '__main__':

    game = Board()
    game.mainloop()