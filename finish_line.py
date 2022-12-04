from pico2d import *

import server
import play_state
from ai import AI
from player import Player


class FinishLine:
    def __init__(self):
        self.bgm = load_music('res/race_bgm.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

        self.image = load_image('res/finish_line.png')
        self.x, self.y = server.background.width - 25, 270
        self.win_sound = load_wav('res/win.wav')
        self.lose_sound = load_wav('res/lose.wav')
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
            self.bgm.stop()
            if type(other) == Player:
                self.win_sound.play()
            elif type(other) == AI:
                self.lose_sound.play()
            play_state.game_over = True
            play_state.winner = other



