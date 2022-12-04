from pico2d import *
import server

class Background:
    def __init__(self):
        self.image = load_image('res/background.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.width = self.image.w
        self.height = self.image.h

        self.window_left = 0
        self.window_bottom = 0



    def update(self):
        self.window_left = clamp(0, int(server.player.x) - self.canvas_width // 2, self.width - self.canvas_width - 1)
        self.window_bottom = clamp(0, int(server.player.y) - self.canvas_height // 2, self.height - self.canvas_height - 1)

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0, 0)



