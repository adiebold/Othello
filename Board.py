import tkinter as tk
from PIL import ImageTk, Image

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

        for x in range(8):
            self.squares.append([])
            for y in range(8):
                self.squares[x].append(tk.Button(self.board, image=self.blank,
                                                 command=lambda x_value=x,y_value=y: self.change_color(x_value, y_value, self.black)))
                self.squares[x][y].grid(row=x, column=y, sticky='news')

    def change_color(self, x, y, color):

        self.squares[x][y].config(image=color, state='disabled')

if __name__ == '__main__':

    game = Board()
    game.mainloop()