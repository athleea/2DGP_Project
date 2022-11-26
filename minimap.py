from pico2d import *

class MiniMap:
    def __init__(self):
        self.image = load_image('res/map.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 580)



