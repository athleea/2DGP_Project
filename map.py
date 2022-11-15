from pico2d import *

import play_state


class Map:
    def __init__(self):
        self.image = load_image('res/map.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 580)

class Pin:
    def __init__(self, player_id):
        self.image = load_image(f'res/pin{player_id+1}.png')
        self.player_id = player_id
        self.ob_x = 200.0
    def update(self):
        self.ob_x = 200.0 + play_state.observer[self.player_id][0] * 0.04
    def draw(self):
        self.image.draw(self.ob_x, 580, 15, 20)