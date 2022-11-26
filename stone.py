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
        if Stone.image is None:
            Stone.image = load_image('res/rock.png')
        self.x, self.y = 800, 50 * random.randint(2,8)
        self.speed = character_data.get_speed_pps(random.randint(1, 5))
        self.frame = 0 

    def draw(self):
        self.image.clip_draw(int(self.frame) * stone['width'], stone['bottom'], stone['width'], stone['height'], self.x, self.y, 32, 46)
        draw_rectangle(*self.get_bb())


    def update(self):
        self.frame = (self.frame + stone['FramePerAction'] * stone['ActionPerTime'] * game_framework.frame_time) % stone['FramePerAction']
        self.x -= self.speed * game_framework.frame_time

        if self.x == 0:
            game_world.remove_object(self)

    def handle_collision(self, other, group):
        game_world.remove_object(self)

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15
