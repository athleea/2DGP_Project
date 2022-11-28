from pico2d import *
import server

class StartLine:

    def __init__(self):
        self.image = load_image('res/start_line.png')
        self.x, self.y = 25, 270

    def update(self):
        pass

    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom

        self.image.draw(sx, sy)
