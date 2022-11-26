from pico2d import *

import background
import character_data
import random
import game_framework
import play_state

key_Idle, key_Run, key_Sturn, key_Skill, key_Speed, key_Cool_Time, key_Hording_Time = range(7)
RAD, RAU, UAD, UAU, DAD, DAU, RD, END_SKILL = range(8)

among, dog, ghost, hulk, human, icarus, kirby, ninja, patrick_star, pikachu, sonic, spiderman, turtle, witch, zombie = range(15)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RAD,
    (SDL_KEYDOWN, SDLK_UP): UAD,
    (SDL_KEYDOWN, SDLK_DOWN): DAD,
    (SDL_KEYDOWN, SDLK_r): RD,
    (SDL_KEYUP, SDLK_RIGHT): RAU,
    (SDL_KEYUP, SDLK_UP): UAU,
    (SDL_KEYUP, SDLK_DOWN): DAU,
}


class IDLE:
    @staticmethod
    def enter(self, event):  # 상태에 들어갈 때 행하는 액션
        print("ENTER IDLE")
        self.dirX, self.dirY = 0, 0
        self.set_state(key_Idle)

    @staticmethod
    def exit(self, event):  # 상태를 나올 때 행하는 액션, 고개 들기
        print("EXIT IDLE")
        pass

    @staticmethod
    def do(self):  # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * game_framework.frame_time) % self.FRAMES_PER_ACTION

    @staticmethod
    def draw(self):
        self.image.clip_draw(int(self.frame) * self.clipWidth, self.clipBottom, self.clipWidth, self.clipHeight, self.x,
                             self.y, 50, 90)


class RUN:
    @staticmethod
    def enter(self, event):
        self.set_state(key_Run)

        if event == RD:
            if self.character[key_Skill] is not None:
                if not self.skilling:
                    if self.cool_time == 0.0 or self.cool_time < game_framework.cur_time:
                        self.skilling = True
                        self.skill_enter_time = game_framework.cur_time
                        self.cool_time = self.character[key_Cool_Time] + self.skill_enter_time
                        self.hording_time = self.character[key_Hording_Time]

    @staticmethod
    def exit(self, event):
        if event == RD:
            self.active_skill()
        pass

    @staticmethod
    def do(self):

        self.frame = (self.frame + self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * game_framework.frame_time) % self.FRAMES_PER_ACTION

        self.x += 1 * self.speed * game_framework.frame_time
        self.y += 0 * self.speed * game_framework.frame_time

        self.y = clamp(90, self.y, 480)

        if self.skill_enter_time + self.hording_time <= game_framework.cur_time:
            self.skilling = False

        if self.sturn_enter_time + self.sturn_time <= game_framework.cur_time:
            self.sturning = False

    @staticmethod
    def draw(self):
        if self.skilling:
            self.set_state(key_Skill)
        elif self.sturning:
            self.set_state(key_Sturn)
            self.character[key_Sturn]["ActionPerTime"] = 2
            self.speed = 0
        else:
            self.set_state(key_Run)

        self.image.clip_draw(int(self.frame) * self.clipWidth, self.clipBottom, self.clipWidth, self.clipHeight, self.x,
                             self.y, 50, 90)


next_state = {
    IDLE: {RAD: RUN, UAD: RUN, DAD: RUN, RAU: RUN, UAU: RUN, DAU: RUN},
    RUN: {RAD: RUN, UAD: RUN, DAD: RUN, RAU: RUN, UAU: RUN, DAU: RUN, RD: RUN, },

}


class AI:

    def add_event(self, event):
        self.event_que.insert(0, event)

    def __init__(self, x=30, y=100):
        self.speed = 0.0
        self.image = None
        self.character = None

        self.x, self.y = x, y
        self.mapX, mapY = 0, 0
        self.dirX, self.dirY = 0, 0
        self.name = ""
        self.frame = 0
        self.FRAMES_PER_ACTION = 0
        self.ACTION_PER_TIME = 0
        self.clipBottom = 0
        self.clipWidth = 0
        self.clipHeight = 0

        self.cool_time = 0.0
        self.hording_time = 0.0
        self.skill_enter_time = 0.0
        self.skilling = False

        self.sturning = False
        self.sturn_enter_time = 0.0
        self.sturn_time = 0.0

        self.event_que = []
        self.cur_state = IDLE
        self.set_random_character()
        self.cur_state.enter(self, None)

    def update(self):
        if play_state.game_start:
            self.cur_state = RUN
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self, )
        # draw_rectangle(*self.get_bb())

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def set_state(self, cur_state):
        self.character = character_data.characters[self.name]
        self.image = load_image('res/{}.png'.format(self.character["name"]))
        self.speed = self.character[key_Speed]

        if self.character[cur_state] is not None:
            self.FRAMES_PER_ACTION = self.character[cur_state]['FramePerAction']
            self.ACTION_PER_TIME = self.character[cur_state]['ActionPerTime']
            self.clipBottom = self.character[cur_state]['bottom']
            self.clipWidth = self.character[cur_state]['width']
            self.clipHeight = self.character[cur_state]['height']

    def set_random_character(self, state=key_Idle):
        l1 = list(character_data.characters.keys())
        self.name = random.choice(l1)
        # self.name = spiderman  # test code

    def active_skill(self):
        pass

    def get_pos(self):
        return self.x, self.y

    def get_bb(self):
        return self.x - 25, self.y - 45, self.x + 25, self.y + 45

    def handle_collision(self, other, group):
        if group == 'ai:stone':
            self.sturn_enter_time = game_framework.cur_time
            self.sturn_time = 3