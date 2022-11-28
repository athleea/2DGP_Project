from pico2d import *

import server
import play_state


class FinishLine:

    def __init__(self):
        self.image = load_image('res/finish_line.png')
        self.x, self.y = server.background.width - 25, 270

    def update(self):
        pass

    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom

        self.image.draw(sx, sy)

    def get_bb(self):
        return self.x - 25, self.y - 212, self.x + 25, self.y + 212

    def handle_collision(self, other, group):
        if group == 'character:finish_line':
            play_state.game_over = True

