import server
import skills
import game_framework

from character import *


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
        self.dirX, self.dirY = 0,0
        self.set_state_image_and_clip_size(key_Idle)

    @staticmethod
    def exit(self, event):
        if event == RD:
            if self.cool_down is False:
                time = game_framework.cur_time
                self.skill_start_time = time
                self.skill_cool_time = self.character_data[key_Cool_Time] + time
        elif event == START_STURN:
            self.sturn_start_time = game_framework.cur_time

    @staticmethod
    def do(self):
        self.frame = (self.frame + self.frame_per_action * self.action_per_time * game_framework.frame_time) % self.frame_per_action

        self.x = clamp(50, self.x, server.background.width - 1 - 25)
        self.y = clamp(100, self.y, server.background.height - 1 - 50)

        if self.skill_cool_time <= game_framework.cur_time:
            self.cool_down = False

    @staticmethod
    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom

        self.image.clip_draw(
            int(self.frame) * self.clip_size[clip_left],
            self.clip_size[clip_bottom],
            self.clip_size[clip_width],
            self.clip_size[clip_height],
            sx, sy, 50, 90)

class RUN:
    @staticmethod
    def enter(self, event):
        self.set_state_image_and_clip_size(key_Run)

        if not self.debuff:
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
        elif event == START_STURN:
            self.sturn_processing = False
            self.sturn_start_time = game_framework.cur_time

    @staticmethod
    def do(self):
        world_cur_time = game_framework.cur_time
        frame_time = game_framework.frame_time

        self.frame = (self.frame + self.frame_per_action * self.action_per_time * frame_time) % self.frame_per_action

        self.x += self.dirX * self.speed * frame_time
        self.y += self.dirY * self.speed * frame_time

        self.x = clamp(50, self.x, server.background.width - 1 - 50)
        self.y = clamp(100, self.y, server.background.height - 1 - 100)

        # 스킬 사용 활성화
        if self.skill_cool_time <= world_cur_time:
            self.cool_down = False

    @staticmethod
    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom


        self.image.clip_draw(
            int(self.frame) * self.clip_size[clip_left],
            self.clip_size[clip_bottom],
            self.clip_size[clip_width],
            self.clip_size[clip_height],
            sx, sy, 50, 90)

class SKILL:
    @staticmethod
    def enter(self, event):

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

        if self.character_data[key_Skill] is not None and self.cool_down is False:
            self.frame = 0
            self.set_state_image_and_clip_size(key_Skill)
            self.skill_application_time = self.character_data[key_Skill_Application_Time]
            skills.use_skill(self)
        else:
            self.add_event(END_SKILL)


    @staticmethod
    def exit(self, event):
        if event == END_SKILL:
            self.cool_down = True
            self.buff = False
            self.skill_processing = False
            skills.use_end_skill(self)
        elif event == START_STURN:
            self.sturn_processing = False
            self.sturn_start_time = game_framework.cur_time


    @staticmethod
    def do(self):
        world_cur_time = game_framework.cur_time
        frame_time = game_framework.frame_time
        self.skill_processing = True

        self.frame = (self.frame + self.frame_per_action * self.action_per_time * frame_time) % self.frame_per_action

        self.x += self.dirX * self.speed * frame_time
        self.y += self.dirY * self.speed * frame_time

        if self.skill_start_time + self.skill_application_time <= world_cur_time:
            self.add_event(END_SKILL)

        if self.skill_start_time + self.action_per_time <= world_cur_time:
            self.set_state_image_and_clip_size(key_Run)

        self.x = clamp(50, self.x, server.background.width - 1 - 50)
        self.y = clamp(100, self.y, server.background.height - 1 - 100)


    @staticmethod
    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom

        self.image.clip_draw(
            int(self.frame) * self.clip_size[clip_left],
            self.clip_size[clip_bottom],
            self.clip_size[clip_width],
            self.clip_size[clip_height],
            sx, sy, 50, 90)

class STURN:
    @staticmethod
    def enter(self, event):
        self.set_state_image_and_clip_size(key_Sturn)
        if self.character_data[key_Sturn] is not None:
            if self.sturn_processing is False:
                self.frame = 0
                self.speed = 0
                self.sturn_processing = True
        else:
            self.add_event(END_STURN)

    @staticmethod
    def exit(self, event):
        if event == END_STURN:
            self.set_default_speed()



    @staticmethod
    def do(self):
        world_cur_time = game_framework.cur_time
        frame_time = game_framework.frame_time

        self.frame = (self.frame + self.frame_per_action * self.action_per_time * frame_time)
        if self.frame >= self.frame_per_action:
            self.frame = self.frame_per_action - 0.1

        #print(self.sturn_start_time, world_cur_time)

        if self.sturn_processing is True and self.sturn_start_time + 2.0 <= world_cur_time:
            self.add_event(END_STURN)


    @staticmethod
    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom

        self.image.clip_draw(
            int(self.frame) * self.clip_size[clip_left],
            self.clip_size[clip_bottom],
            self.clip_size[clip_width],
            self.clip_size[clip_height],
            sx, sy, 50, 90)

next_state = {
    IDLE: {RAD: RUN, UAD: RUN, DAD: RUN, RAU: RUN, UAU: RUN, DAU: RUN, RD: SKILL, END_SKILL: IDLE, START_STURN: STURN, END_STURN:IDLE},
    RUN: {RAD: RUN, UAD: RUN, DAD: RUN, RAU: RUN, UAU: RUN, DAU: RUN, RD: SKILL, END_SKILL: RUN, START_STURN: STURN ,END_STURN:RUN},
    SKILL: {RAD: SKILL, UAD: SKILL, DAD: SKILL, RAU: SKILL, UAU: SKILL, DAU: SKILL, RD: SKILL, END_SKILL: RUN, START_STURN: STURN},
    STURN: {RAD: STURN, UAD: STURN, DAD: STURN, RAU: STURN, UAU: STURN, DAU: STURN, RD: STURN, END_STURN: RUN, START_STURN: STURN},
}

class AI(Character):
    def __init__(self, char_id, y):
        super().__init__(char_id, y)
        self.char_id_font = load_font('res/NanumGothic.TTF', 15)
        self.cur_state = IDLE
        self.cur_state.enter(self, None)


    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            print(self.character_name, self.event_que)
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom

        self.char_id_font.draw(sx - 25, sy + 50, f'Player {self.char_id}', font_color[self.char_id - 1])

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def handle_collision(self, other, group):
        if group == 'character:stone':
            pass