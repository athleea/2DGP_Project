from pico2d import *
import random
import game_world
import character_data
import game_framework
import server
from character import START_STURN

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
        self.x, self.y = random.randint(1000, 9900), 90 * random.randint(1, 5)
        self.speed = character_data.get_speed_pps(random.randint(2, 5))
        self.frame = 0

    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom

        self.image.clip_draw(int(self.frame) * stone['width'], stone['bottom'], stone['width'], stone['height'], sx, sy, 32, 46)

    def update(self):
        self.frame = (self.frame + stone['FramePerAction'] * stone['ActionPerTime'] * game_framework.frame_time) % stone['FramePerAction']

        self.x -= self.speed * game_framework.frame_time
        self.x = clamp(0, self.x, server.background.width - 1 - 50)

        if self.x == 0:
            game_world.remove_object(self)

    def handle_collision(self, other, group):
        other.add_event(START_STURN)
        game_world.remove_object(self)

    def get_bb(self):
        return self.x - 16, self.y - 23, self.x + 16, self.y + 23
