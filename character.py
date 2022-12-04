import random
from character_data import *
from pico2d import *

RAD, RAU, UAD, UAU, DAD, DAU, RD, END_SKILL, START_STURN, END_STURN = range(10)
clip_left, clip_bottom, clip_width, clip_height = range(4)

font_color = [(255,0,0), (0,0,255), (255,255,0), (0,255,0), (255,255,255)]

class Character:
    def __init__(self, char_id, y):
        self.char_id = char_id
        self.image = None
        self.frame = 0
        self.clip_size = {clip_left: 0, clip_bottom: 0, clip_width: 0, clip_height: 0}
        self.frame_per_action = 0
        self.action_per_time = 0

        self.character_code = None
        self.character_name = ""
        self.character_data = None
        self.x, self.y = 50, y
        self.dirX, self.dirY = 0, 0
        self.speed = 0.0
        self.cur_state = None

        self.cool_down = False
        self.skill_processing = False
        self.skill_cool_time = 0
        self.skill_start_time = 0
        self.skill_end_time = 0
        self.skill_application_time = 0.0

        self.sturn_processing = False
        self.sturn_start_time = 0

        self.buff = False
        self.debuff = []

        self.event_que = []

        self.set_random_character()
        self.set_state_image_and_clip_size(key_Idle)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def set_speed(self, value):
        self.speed = value

    def set_default_speed(self):
        self.speed = self.character_data[key_Speed]


    def set_clip_size(self, left, bottom, width, height):
        self.clip_size[clip_left] = left
        self.clip_size[clip_bottom] = bottom
        self.clip_size[clip_width] = width
        self.clip_size[clip_height] = height

    def set_character_data(self, character_code):
        self.character_code = character_code
        self.character_data = characters[character_code]
        self.character_name = self.character_data['name']

    def set_random_character(self, state=key_Idle):
        random_name = random.choice(list(characters.keys()))
        # self.set_character_data(sonic)
        self.set_character_data(random_name)
        self.set_state_image_and_clip_size(state)
        self.set_default_speed()
        self.debuff.clear()

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

    def get_x(self):
        return self.x

    def get_bb(self):
        return self.x - 25, self.y - 45, self.x + 25, self.y + 45