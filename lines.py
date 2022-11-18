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

    def __init__(self, x=200):
        self.image = load_image('res/transform_line.png')
        self.x = x
        self.y = 267
        self.t_list = []

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, 267)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 25, self.y - 212, self.x+25, self.y+212

    def handle_collision(self, other, group):
        if group == 'player:t_line':
            if not self.check_in_t_list(other):
                self.t_list.append(other)
                other.set_random_character()
            pass

    def check_in_t_list(self, player):
        return player in self.t_list

class FinishLine:

    def __init__(self):
        self.image = load_image('res/finish_line.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(9975 - background.mapX, 267)
