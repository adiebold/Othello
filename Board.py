import tkinter as tk
from PIL import ImageTk, Image
from collections import namedtuple

class Board(tk.Tk):

    Sqr = namedtuple('Square', 'button x y')
    squares = []

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.geometry(self, '+100+100')

        self.board = tk.Frame(self, bg = 'blue')
        self.board.pack(side='top', fill='both', expand=True)

        self.create_button_images()

        self.squares = []
        self.create_squares()

    def create_button_images(self):

        self.blank = ImageTk.PhotoImage(Image.open('blank.jpg'))
        self.red = ImageTk.PhotoImage(Image.open('red.jpg'))
        self.black = ImageTk.PhotoImage(Image.open('black.jpg'))

    def create_squares(self):

        for x in range(8):
            for y in range(8):
                self.squares.append(self.Sqr(tk.Button(self.board, image=self.blank, command=s)))

                # self.squares[x].append(tk.Button(self.board, image=self.blank, command=self.turn_black))
                # # self.squares[x][y].pack(expand=True)
                # self.squares[x][y].grid(row=x, column=y, sticky='news')
                # self.squares[x][y].config(image=self.red)

    def turn_black(self):

        print(type(self))

if __name__ == '__main__':

    game = Board()
    game.mainloop()