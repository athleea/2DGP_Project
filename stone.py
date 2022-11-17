import random
from pico2d import *
import game_world
import character_data
import game_framework

stone = {
    "ActionPerTime": 1.0 / 0.5,
    "FramePerAction": 15,
    "bottom": 0,
    "width": 16,
    "height": 23
}


class Stone:
    image = None

    def __init__(self):
        if Stone.image == None:
            Stone.image = load_image('res/rock.png')
        self.x, self.y = 800, random.randint(100, 480)
        self.fall_speed = character_data.get_speed_pps(random.randint(1, 3))
        self.frame = 0 

    def draw(self):
        self.image.clip_draw(int(self.frame) * stone['width'], stone['bottom'], stone['width'], stone['height'], self.x, self.y, 32, 46)
        draw_rectangle(*self.get_bb())


    def update(self):
        self.frame = (self.frame + stone['FramePerAction'] * stone['ActionPerTime'] * game_framework.frame_time) % stone['FramePerAction']
        self.x -= self.fall_speed * game_framework.frame_time

    def handle_collision(self, other, group):
        if group == 'player:stone':
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 16, self.y - 23, self.x + 16, self.y + 23
