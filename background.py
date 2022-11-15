from pico2d import *

mapX = 400

class Background:
    def __init__(self):
        self.image = load_image('res/background.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(mapX, 300)
