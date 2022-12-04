import game_world
import server
import skills
import game_framework
from BehaviorTree import *

from character import *
from character_data import PIXEL_PER_METER
from fireball import FireBall
from knife import Knife
from stone import Stone

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

    @staticmethod
    def exit(self, event):
        if event == START_STURN:
            self.sturn_processing = False
            self.sturn_start_time = game_framework.cur_time

    @staticmethod
    def do(self):
        world_cur_time = game_framework.cur_time
        frame_time = game_framework.frame_time

        self.frame = (self.frame + self.frame_per_action * self.action_per_time * frame_time) % self.frame_per_action

        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time

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

        if self.character_data[key_Skill] is not None:
            if self.skill_processing is False and self.cool_down is False:
                start_time = game_framework.cur_time
                self.frame = 0

                self.cool_down = True
                self.skill_cool_time = start_time + self.character_data[key_Cool_Time]


                self.skill_processing = True
                self.skill_start_time = start_time

                self.skill_application_time = self.character_data[key_Skill_Application_Time]
                self.set_state_image_and_clip_size(key_Skill)
                skills.use_skill(self)


        else:
            self.add_event(END_SKILL)


    @staticmethod
    def exit(self, event):
        if event == END_SKILL:
            skills.use_end_skill(self)
            self.buff = False
            self.skill_processing = False

        elif event == START_STURN:
            self.buff = False
            self.skill_processing = False
            self.sturn_processing = False
            self.sturn_start_time = game_framework.cur_time


    @staticmethod
    def do(self):
        world_cur_time = game_framework.cur_time
        frame_time = game_framework.frame_time

        self.frame = (self.frame + self.frame_per_action * self.action_per_time * frame_time) % self.frame_per_action

        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time

        if self.skill_start_time + self.skill_application_time <= world_cur_time:
            self.add_event(END_SKILL)

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

        if self.character_data[key_Sturn] is not None:
            if self.sturn_processing is False:
                self.frame = 0
                self.speed = 0
                self.sturn_processing = True
        else:
            self.add_event(END_STURN)

        self.set_state_image_and_clip_size(key_Sturn)

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
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
        self.dir = 0
        self.bt = None
        self.build_behavior_tree()

    def check_cool_time(self):
        if self.character_data[key_Skill] is None or self.cool_down is True:
            return BehaviorTree.FAIL
        else:
            return BehaviorTree.SUCCESS
    def use_skill(self):
        self.add_event(RD)

    def move_to_finish_line(self):
        self.tx = 10000
        self.dir = 0
        return BehaviorTree.SUCCESS

    def fine_obstruction(self):
        shortest_distance = 10000 ** 2
        target_obstruction = None
        for obj in game_world.all_objects():
            if type(obj) is Stone or type(obj) is FireBall or type(obj) is Knife:
                distance = (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2
                if distance < (PIXEL_PER_METER * 1) ** 2 and distance < shortest_distance:
                    target_obstruction = obj
                    shortest_distance = distance
        if target_obstruction is not None and target_obstruction.owner_id != self.char_id :
            if target_obstruction.y >= self.y:
                if self.y <= 150:
                    self.dir = 45
                else:
                    self.dir = -45
            else:
                if self.y >= server.background.height - 1 - 150:
                    self.dir = -45
                else:
                    self.dir = 45
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def build_behavior_tree(self):
        check_cool_time = Leaf('Check Cool Time', self.check_cool_time)
        use_skill = Leaf('Use Skill', self.use_skill)
        using_skill = Sequence('Using Skill', check_cool_time, use_skill)

        flee_obstruction = Leaf('Flee Obstruction', self.fine_obstruction)

        move_to_finish_line = Leaf('Move', self.move_to_finish_line)


        root = Selector('Goal Finish Line', using_skill, flee_obstruction, move_to_finish_line)
        self.bt = BehaviorTree(root)

    def update(self):
        self.bt.run()
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def handle_collision(self, other, group):
        if group == 'character:stone':
            self.add_event(START_STURN)