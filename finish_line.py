from pico2d import *

import game_framework
import end_state
import play_state


class FinishLine:

    def __init__(self):
        self.image = load_image('res/finish_line.png')
        self.x = 700
        self.y = 267

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, 267)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 25, self.y - 212, self.x + 25, self.y + 212

    def handle_collision(self, other, group):
        if group == 'character:finish_line':
            play_state.game_over = True

