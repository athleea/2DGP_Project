from pico2d import *
import game_world
import character_data
import game_framework
import server
from character import START_STURN

class Knife:
    image = None

    def __init__(self, x, y):
        if Knife.image is None:
            Knife.image = load_image('res/knife.png')
        self.start_x = x
        self.x, self.y = x, y
        self.speed = character_data.get_speed_pps(5)
        self.frame = 0

    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom

        self.image.draw(sx, sy)

    def update(self):
        self.x += self.speed * game_framework.frame_time
        self.x = clamp(0, self.x, server.background.width - 1 - 50)

        if self.x >= 10000 or self.x >= self.start_x + 1000:
            game_world.remove_object(self)

    def handle_collision(self, other, group):
        if group == "character:throws":
            other.add_event(START_STURN)
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 12, self.y - 6, self.x + 12, self.y + 6
