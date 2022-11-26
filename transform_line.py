from pico2d import *
from character_data import key_Run


class TransformLine:

    def __init__(self, x=300):
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
        return self.x - 25, self.y - 212, self.x + 25, self.y + 212

    def handle_collision(self, other, group):
        if group == 'character:transform_line':
            if not self.check_in_t_list(other):
                self.t_list.append(other)
                other.set_random_character(key_Run)

    def check_in_t_list(self, player):
        return player in self.t_list
