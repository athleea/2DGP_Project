from pico2d import *
from skills import *

import game_world
import character_data
import random
import game_framework

key_Idle, key_Run, key_Sturn, key_Skill, key_Speed, key_Cool_Time, key_Skill_Application_Time, key_Skill_Text = range(8)

RAD, RAU, UAD, UAU, DAD, DAU, RD, END_SKILL = range(8)
among, dog, ghost, hulk, human, icarus, kirby, ninja, patrick_star, pikachu, sonic, spiderman, turtle, witch, zombie = range(
    15)
clip_left, clip_bottom, clip_width, clip_height = range(4)

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
    def enter(self, event):
        self.set_state_image_and_clip_size(key_Idle)
        self.skill_processing = False

    @staticmethod
    def exit(self, event):
        if event == RD:
            if self.cool_down is False:
                time = game_framework.cur_time
                self.skill_start_time = time
                self.skill_cool_time = self.character_data[key_Cool_Time] + time

    @staticmethod
    def do(self):
        self.frame = (
                             self.frame + self.frame_per_action * self.action_per_time * game_framework.frame_time) % self.frame_per_action

        if self.skill_cool_time <= game_framework.cur_time:
            self.cool_down = False

    @staticmethod
    def draw(self):
        self.image.clip_draw(
            int(self.frame) * self.clip_size[clip_left],
            self.clip_size[clip_bottom],
            self.clip_size[clip_width],
            self.clip_size[clip_height],
            self.x, self.y, 50, 90)


class RUN:
    @staticmethod
    def enter(self, event):
        self.set_state_image_and_clip_size(key_Run)
        self.speed = self.character_data[key_Speed]

        if event == RAD:
            self.dirX += 1
        elif event == UAD:
            self.dirY += 1
        elif event == DAD:
            self.dirY += -1

        elif event == RAU:
            self.dirX = 0
        elif event == UAU:
            self.dirY += -1
        elif event == DAU:
            self.dirY += 1

    @staticmethod
    def exit(self, event):
        if event == RD:
            if self.cool_down is False:
                time = game_framework.cur_time
                self.skill_start_time = time
                self.skill_cool_time = self.character_data[key_Cool_Time] + time

    @staticmethod
    def do(self):
        self.frame = (
                             self.frame + self.frame_per_action * self.action_per_time * game_framework.frame_time) % self.frame_per_action

        self.x += self.dirX * self.speed * game_framework.frame_time
        self.y += self.dirY * self.speed * game_framework.frame_time

        self.y = clamp(90, self.y, 480)

        # 스킬 사용 활성화
        if self.skill_cool_time <= game_framework.cur_time:
            self.cool_down = False

    @staticmethod
    def draw(self):
        self.image.clip_draw(
            int(self.frame) * self.clip_size[clip_left],
            self.clip_size[clip_bottom],
            self.clip_size[clip_width],
            self.clip_size[clip_height],
            self.x, self.y, 50, 90)


class SKILL:
    @staticmethod
    def enter(self, event):  # 상태에 들어갈 때 행하는 액션
        if event == RAD:
            self.dirX += 1
        elif event == UAD:
            self.dirY += 1
        elif event == DAD:
            self.dirY += -1

        elif event == RAU:
            self.dirX += -1
        elif event == UAU:
            self.dirY += -1
        elif event == DAU:
            self.dirY += 1

        if self.skill_processing is True:
            self.set_state_image_and_clip_size(key_Skill)
            self.skill_application_time = self.character_data[key_Skill_Application_Time]
        elif self.character_data[key_Skill] is not None and self.cool_down is False:
            self.set_state_image_and_clip_size(key_Skill)
            self.skill_application_time = self.character_data[key_Skill_Application_Time]
        else:
            self.add_event(END_SKILL)

    @staticmethod
    def exit(self, event):
        pass

    @staticmethod
    def do(self):
        self.skill_processing = True
        self.frame = (
                             self.frame + self.frame_per_action * self.action_per_time * game_framework.frame_time) % self.frame_per_action

        if self.skill_start_time + self.skill_application_time <= game_framework.cur_time:
            self.cool_down = True
            self.add_event(END_SKILL)

        self.x += self.dirX * self.speed * game_framework.frame_time
        self.y += self.dirY * self.speed * game_framework.frame_time

        self.y = clamp(90, self.y, 480)

    @staticmethod
    def draw(self):
        self.image.clip_draw(
            int(self.frame) * self.clip_size[clip_left],
            self.clip_size[clip_bottom],
            self.clip_size[clip_width],
            self.clip_size[clip_height],
            self.x, self.y, 50, 90)


next_state = {
    IDLE: {RAD: RUN, UAD: RUN, DAD: RUN, RAU: RUN, UAU: RUN, DAU: RUN, RD: SKILL, END_SKILL: IDLE},
    RUN: {RAD: RUN, UAD: RUN, DAD: RUN, RAU: RUN, UAU: RUN, DAU: RUN, RD: SKILL, END_SKILL: RUN},
    SKILL: {RAD: SKILL, UAD: SKILL, DAD: SKILL, RAU: SKILL, UAU: SKILL, DAU: SKILL, RD: SKILL, END_SKILL: RUN}
}


class Character:
    def __init__(self, x, y):
        self.image = None
        self.frame = 0
        self.clip_size = {clip_left: 0, clip_bottom: 0, clip_width: 0, clip_height: 0}
        self.frame_per_action = 0
        self.action_per_time = 0

        self.character_name = ""
        self.character_data = None
        self.x, self.y = x, y
        self.dirX, self.dirY = 0, 0
        self.speed = 0.0
        self.cur_state = IDLE

        self.cool_down = False
        self.skill_processing = False
        self.skill_cool_time = 0
        self.skill_start_time = 0
        self.skill_end_time = 0
        self.skill_application_time = 0.0

        self.event_que = []

    def add_event(self, event):
        self.event_que.insert(0, event)

    def set_speed(self):
        self.speed = self.character_data[key_Speed]

    def set_clip_size(self, left, bottom, width, height):
        self.clip_size[clip_left] = left
        self.clip_size[clip_bottom] = bottom
        self.clip_size[clip_width] = width
        self.clip_size[clip_height] = height

    def set_character_data(self, character_name):
        self.character_data = character_data.characters[character_name]
        self.character_name = character_name

    def set_random_character(self, state=key_Idle):
        random_name = random.choice(list(character_data.characters.keys()))
        # self.set_character_data(sonic)
        self.set_character_data(random_name)
        self.set_state_image_and_clip_size(state)
        self.set_speed()
        self.cool_down = False
        self.skill_processing = False
        self.skill_cool_time = 0
        self.skill_start_time = 0
        self.skill_end_time = 0
        self.skill_application_time = 0.0

    def set_state_image_and_clip_size(self, state=key_Idle):
        self.image = load_image('res/{}.png'.format(self.character_data['name']))
        if self.character_data[state] is not None:
            self.frame_per_action = self.character_data[state]['FramePerAction']
            self.action_per_time = self.character_data[state]['ActionPerTime']
            self.set_clip_size(
                left=self.character_data[state]['width'],
                bottom=self.character_data[state]['bottom'],
                width=self.character_data[state]['width'],
                height=self.character_data[state]['height'],
            )

    def get_pos(self):
        return self.x, self.y

    def get_bb(self):
        return self.x - 25, self.y - 45, self.x + 25, self.y + 45


class Player(Character):
    def __init__(self, x=30, y=100):
        super().__init__(x, y)
        self.set_random_character()
        self.set_state_image_and_clip_size(key_Idle)
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        # draw_rectangle(*self.get_bb())

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def handle_collision(self, other, group):
        if group == 'character:stone':
            pass