import time

from pico2d import *
import game_framework

class Timer:
    def __init__(self):
        self.timeText = load_font('res/ENCR10B.TTF', 20)
        self.enterTime = time.time()
        self.time = 0.0

    def draw(self):
        self.timeText.draw(720, 580, f'{self.time:.2f}')

    def update(self):
        self.time = time.time() - self.enterTime - 3