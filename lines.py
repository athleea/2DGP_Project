from pico2d import *
import background

class StartLine:

    def __init__(self):
        self.image = load_image('res/start_line.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(25 - background.mapX, 267)


class TransformLine:

    def __init__(self, x=1500):
        self.image = load_image('res/transform_line.png')
        self.x = x

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x - background.mapX, 267)


class FinishLine:

    def __init__(self):
        self.image = load_image('res/finish_line.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(9975 - background.mapX, 267)
