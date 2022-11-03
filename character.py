from pico2d import *
import character_data
import random

RAD, RAU, UAD, UAU, DAD, DAU, RD, RU  = range(8)

NUM_IDLE, NUM_RUN, NUM_STURN, NUM_SKILL = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RAD,
    (SDL_KEYDOWN, SDLK_UP): UAD,
    (SDL_KEYDOWN, SDLK_DOWN): DAD,
    (SDL_KEYDOWN, SDLK_r): RD,
    (SDL_KEYUP, SDLK_RIGHT): RAU,
    (SDL_KEYUP, SDLK_UP): UAU,
    (SDL_KEYUP, SDLK_DOWN): DAU,
    (SDL_KEYUP, SDLK_r): RU
}


class IDLE:
    @staticmethod
    def enter(self, event): # 상태에 들어갈 때 행하는 액션
        #print("ENTER IDLE")
        self.dirY = 0
        self.dirX = 0
        self.cur_state_num = NUM_IDLE
        self.set_character()

    @staticmethod
    def exit(self): # 상태를 나올 때 행하는 액션, 고개 들기
        print("EXIT IDLE")

    @staticmethod
    def do(self): # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + 1) % self.frameCount
       
    @staticmethod
    def draw(self):
        self.image.clip_draw(self.frame*self.clipWidth, self.clipBottom,
         self.clipWidth, self.clipHeight, self.x, self.y, 50, 90)


class RUN:
    @staticmethod
    def enter(self, event):
        #print("ENTER RUN")
        self.cur_state_num = NUM_RUN
        self.set_character()
        
        if event == RAD:
            self.dirX += 1
        elif event == UAD:
            self.dirY += 1
        elif event == DAD:
            self.dirY -= 1

        elif event == RAU:
            self.dirX -= 1
        elif event == UAU:
            self.dirY -= 1
        elif event == DAU:
            self.dirY += 1

    @staticmethod
    def exit(self):
        print("EXIT RUN")

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % self.frameCount
        # x 좌표 변경, 달리기
        self.x += self.dirX * self.speed
        self.y += self.dirY * self.speed
        self.y = clamp(90, self.y, 520)

    @staticmethod
    def draw(self):
        self.image.clip_draw(self.frame*self.clipWidth, self.clipBottom,
         self.clipWidth, self.clipHeight, self.x, self.y, 50, 90)
        


next_state = {
    IDLE: {RAD: RUN, UAD: RUN, DAD: RUN, RAU: RUN, UAU: RUN, DAU: RUN},
    RUN: {RAD: IDLE, UAD: IDLE, DAD: IDLE, RAU: IDLE, UAU: IDLE, DAU: IDLE},

}


class Character:

    def add_event(self, event):
        self.event_que.insert(0, event)

    def __init__(self):
        self.x, self.y = 30, 90
        self.dirX, self.dirY = 0, 0
        self.name = ""
        self.speed = 0
        self.frame = 0
        self.frameCount = 0
        self.clipBottom = 0
        self.clipWidth = 0
        self.clipHeight = 0

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state_num = NUM_IDLE
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

        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self,)
        delay(0.05)

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
    
    def set_character(self):
        self.image = load_image('res/{}.png'.format(self.name))
        self.character = character_data.characters[self.name]

        self.frame = 0
        self.frameCount = self.character[self.cur_state_num]['frame']
        self.clipBottom = self.character[self.cur_state_num]['bottom']
        self.clipWidth = self.character[self.cur_state_num]['width']
        self.clipHeight = self.character[self.cur_state_num]['height']

        self.speed = self.character['speed']
        
    def set_random_character(self):
        l1 = list(character_data.characters.keys())
        rand = random.randint(0, len(l1)-1)
        self.name = l1[rand]

        
        
