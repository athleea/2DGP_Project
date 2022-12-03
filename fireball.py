from pico2d import *
import random
import game_world
import character_data
import game_framework
import server
from character import START_STURN

fire_ball = {
    "ActionPerTime": 1,
    "FramePerAction": 4,
    "bottom": 0,
    "width": 24,
    "height": 24,
}


class FireBall:
    image = None

    def __init__(self, x, y):
        if FireBall.image is None:
            FireBall.image = load_image('res/fireball.png')
        self.start_x = x
        self.x, self.y = x, y
        self.speed = character_data.get_speed_pps(5)
        self.frame = 0

    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom

        self.image.clip_draw(int(self.frame) * fire_ball['width'], fire_ball['bottom'], fire_ball['width'], fire_ball['height'], sx, sy, 30, 30)

    def update(self):
        self.frame = (self.frame + fire_ball['FramePerAction'] * fire_ball['ActionPerTime'] * game_framework.frame_time) % fire_ball['FramePerAction']

        self.x += self.speed * game_framework.frame_time
        self.x = clamp(0, self.x, server.background.width - 1 - 50)

        if self.x >= 10000 or self.x >= self.start_x + 1000:
            game_world.remove_object(self)

    def handle_collision(self, other, group):
        if group == "character:throws":
            print("collision")
            other.add_event(START_STURN)
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15
