#!/usr/bin/env python3

# https://www.tutorialspoint.com/how-to-move-an-image-in-tkinter-canvas-with-arrow-keys


# Import the required libraries
from tkinter import *
from PIL import Image, ImageTk


class App():
    def __init__(self):
        self.height = 500
        self.width = 500
        self.window = Tk()
        self.window.geometry(f"{self.width}x{self.height}")

        self.canvas = Canvas(
            self.window,
            width=self.width,
            height=self.height,
            bg="black"
        )
        self.canvas.pack()

        self.window.after(1000, self.start_game)
        self.window.mainloop()


    def random_position(self):
        x = min + (max - min) * random()
        y = min + (max - min) * random()
        return (x, y)


    def start_game(self):
        self.clear_canvas()

        #self.draw_image("images/player.png", self.get_canvas_center_x(), self.get_canvas_center_y())
        self.window.after(1000, self.start_game)


    def draw_image(self, image_path, x, y):
        return self.canvas.create_image(
            x,
            y,
            image=ImageTk.PhotoImage(
                Image.open(image_path)
            )
        )

    def move_image(self, image_id, x, y):
        self.canvas.move(image_id, x, y)

    def clear_canvas(self):
        self.canvas.delete("all")

    def get_canvas_coords(self, image_id):
        return self.canvas.coords(image_id)

    def get_canvas_height(self):
        return self.height

    def get_canvas_width(self):
        return self.width

    def get_canvas_center(self):
        return self.width/2, self.height/2

    def get_canvas_center_x(self):
        return self.width/2


if __name__ == "__main__":
    app = App()

