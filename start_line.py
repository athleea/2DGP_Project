from pico2d import *


class StartLine:

    def __init__(self):
        self.image = load_image('res/start_line.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(25, 267)
