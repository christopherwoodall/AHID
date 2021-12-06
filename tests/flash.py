#!/usr/bin/env python3

from tkinter import *
from PIL import Image, ImageTk
import random
import math


class App():
    def __init__(self):
        self.height = 500
        self.width = 500
        self.window = Tk()
        self.window.resizable(False, False)
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.configure(background='black')
        self.window.title("FLASH")

        self.canvas = Canvas(
            self.window,
            width=self.width,
            height=self.height,
            bg="black"
        )
        self.canvas.pack()
        self.canvas.focus_set()
        self.canvas.bind("<Button-1>", self._clicked)

        good_img = PhotoImage(file="good.png")
        bad_img  = PhotoImage(file="bad.png")
        good = self.canvas.create_image(
            100, 100,
            anchor=NW,
            image=good_img,
            tags=("good")
        )
        bad  = self.canvas.create_image(200, 200, anchor=NW, image=bad_img)
        self.pieces = {
            "good": good,
            "bad": bad
        }

        self.window.after(500, self.start_game)
        self.window.mainloop()


    def start_game(self):
        for name, image_id in self.pieces.items():
            self.move_piece(image_id)
        self.window.after(500, self.start_game)


    def move_piece(self, image_id):
        current_x, current_y = self.canvas.coords(image_id)
        x1, y1, x2, y2 = self.canvas.bbox(image_id)
        #print(self.canvas.bbox(image_id))
        # TODO - make sure the image doesn't go off screen.
        x = math.floor(random.randint(-15, 15))
        y = math.floor(random.randint(-15, 15))

        if y1 < 0:
            y = math.floor(random.randint(5, 15))
        if y2 > self.height:
            y = math.floor(random.randint(-15, -5))
        if x1 < 0:
            x = math.floor(random.randint(5, 15))
        if x2 > self.width:
            x = math.floor(random.randint(-15, -5))

        self.canvas.move(image_id, x, y)
        self.window.update()


    def _clicked(self, event):
        x, y = event.x, event.y
        for name, image_id in self.pieces.items():
            x1, y1, x2, y2 = self.canvas.bbox(image_id)
            if x1 <= x <= x2 and y1 <= y <= y2:
                print(f"{name} was clicked")



if __name__ == "__main__":
    app = App()
