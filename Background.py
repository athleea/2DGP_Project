from pico2d import *

mapX, mapY = 0, 300

class Background:
    def __init__(self):
        
        self.image = load_image('res/background.png')

    def draw(self):
        global mapX, mapY
        self.image.rotate_draw(0, mapX, mapY)