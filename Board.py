import tkinter as tk
from PIL import ImageTk, Image
import os

class Board(tk.Tk):



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

        # frame1 = tk.Frame(self.board, bg = 'red')
        # # frame1.pack(fill=tk.BOTH, expand=1)
        # frame1.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)
        # # frame1.grid(row=0,column=0)
        # label = tk.Label(frame1, text='test')
        # label.pack()

        for x in range(8):
            self.squares.append([])
            for y in range(8):
                self.squares[x].append(tk.Button(self.board, image=self.blank))
                # self.squares[x][y].pack(expand=True)
                print(x, ' and ', y)
                self.squares[x][y].grid(row=x, column=y, sticky='news')


if __name__ == '__main__':

    game = Board()
    game.mainloop()