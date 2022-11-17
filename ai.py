from pico2d import *

import game_world
import character_data
import random
import game_framework
import play_state

key_Idle, key_Run, key_Sturn, key_Skill, key_Speed, key_Cool_Time = range(6)

class IDLE:
    @staticmethod
    def enter(self, event):  # 상태에 들어갈 때 행하는 액션
        self.dirX, self.dirY = 0, 0

        self.cur_state_num = key_Idle
        self.set_character()

    @staticmethod
    def exit(self):  # 상태를 나올 때 행하는 액션, 고개 들기
        # print("EXIT IDLE")
        pass

    @staticmethod
    def do(self):  # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * game_framework.frame_time) % self.FRAMES_PER_ACTION

    @staticmethod
    def draw(self):
        self.image.clip_draw(int(self.frame) * self.clipWidth, self.clipBottom, self.clipWidth, self.clipHeight, self.x, self.y, 50, 90)


class RUN:
    @staticmethod
    def enter(self, event):
        # print("ENTER RUN")
        self.cur_state_num = key_Run
        self.set_character()

    @staticmethod
    def exit(self):
        # print("EXIT RUN")
        pass

    @staticmethod
    def do(self):
        # x 좌표 변경, 달리기
        self.frame = (self.frame + self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * game_framework.frame_time) % self.FRAMES_PER_ACTION

        self.x += 1 * self.speed * game_framework.frame_time
        self.y += 0 * self.speed * game_framework.frame_time

        # background.mapX -= self.dirX * self.speed * game_framework.frame_time
        self.x = clamp(0, self.x, 10000)
        self.y = clamp(90, self.y, 480)

    @staticmethod
    def draw(self):
        self.image.clip_draw(int(self.frame) * self.clipWidth, self.clipBottom,
                             self.clipWidth, self.clipHeight, self.x, self.y, 50, 90)


next_state = {
}


class AI:

    def add_event(self, event):
        self.event_que.insert(0, event)

    def __init__(self, x=30, y=500):
        self.image = None
        self.character = None
        self.x, self.y = x, y
        self.dirX, self.dirY = 0, 0
        self.name = ""
        self.frame = 0
        self.FRAMES_PER_ACTION = 0
        self.ACTION_PER_TIME = 0
        self.clipBottom = 0
        self.clipWidth = 0
        self.clipHeight = 0

        self.event_que = []
        self.cur_state = RUN
        self.cur_state_num = key_Idle
        self.set_random_character()
        self.cur_state.enter(self, None)


    def update(self):
        self.cur_state.do(self)

        # 이벤트를 확인해서, 이벤트가 있으면 변환 처리
        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, )
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self, )

    def set_character(self):
        self.character = character_data.characters[self.name]
        self.image = load_image('res/{}.png'.format(self.character["name"]))

        self.FRAMES_PER_ACTION = self.character[self.cur_state_num]['FramePerAction']
        self.ACTION_PER_TIME = self.character[self.cur_state_num]['ActionPerTime']
        self.clipBottom = self.character[self.cur_state_num]['bottom']
        self.clipWidth = self.character[self.cur_state_num]['width']
        self.clipHeight = self.character[self.cur_state_num]['height']

        self.speed = self.character[key_Speed]

    def set_random_character(self):
        l1 = list(character_data.characters.keys())
        self.name = random.choice(l1)
    
    def handle_collision(self, other, group):
        if group == 'ai:stone':
            print("collide")
    
    def get_pos(self):
        return self.x, self.y

    def get_bb(self):
        return self.x - 25, self.y - 45, self.x+25, self.y+45
        


