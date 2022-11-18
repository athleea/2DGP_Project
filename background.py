from pico2d import *

mapX = 0

class Background:
    def __init__(self):
        self.image = load_image('res/background.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(30 - mapX, 300)
