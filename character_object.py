from pico2d import *
import time

characters ={
    'Patrick_Star' : {
        "size" : [50, 70],
        0 : {"frame" : 7, "left" : 8, "bottom" : 120, "width" : 30, "height" : 50},     #idle
        1 : {"frame" : 9, "left" : 8, "bottom" : 60, "width" : 32, "height" : 50},      #run
        2 : {"frame" : 4, "left" : 8, "bottom" : 0, "width" : 40, "height" : 50},       #sturn
        3 : None,                                                                       #skill
        "speed" : 4,
        "cooldown_time" : 0,
        "hording_time" : 0,
    },'sonic' : {
        "size" : [50, 70],
        0 : {"frame" : 4, "bottom" : 174, "width" : 30, "height" : 40},     #idle
        1 : {"frame" : 8, "bottom" : 126, "width" : 42, "height" : 38},      #run
        2 : {"frame" : 2, "bottom" : 71, "width" : 40, "height" : 45},       #sturn
        3 : {"frame" : 5, "bottom" : 37, "width" : 34, "height" : 34},
        "speed" : 6,
        "cooldown_time" : 10,
        "hording_time" : 3,
    },'hulk' : {
        "size" : [50, 70],
        0 : {"frame" : 3, "bottom" : 200, "width" : 60, "height" : 90},     #idle
        1 : {"frame" : 6, "bottom" : 100, "width" : 90, "height" : 90},      #run
        2 : {"frame" : 5, "bottom" : 0, "width" : 100, "height" : 90},       #sturn
        3 : None,
        "speed" : 2,
        "cooldown_time" : 0,
        "hording_time" : 0,
    },'kirky' : {
        "size" : [50, 70],
        0 : {"frame" : 6, "bottom" : 100, "width" : 43, "height" : 38},     #idle
        1 : {"frame" : 4, "bottom" : 52, "width" : 48, "height" : 38},      #run
        2 : {"frame" : 4, "bottom" : 0, "width" : 42, "height" : 42},       #sturn
        3 : None,
        "speed" : 2,
        "cooldown_time" : 0,
        "hording_time" : 0,
    },'turtle' : {
        "size" : [50, 70],
        0 : {"frame" : 5, "bottom" : 56, "width" : 70, "height" : 47},     #idle
        1 : {"frame" : 6, "bottom" : 0, "width" : 70, "height" : 46},      #run
        2 : None,
        3 : None,
        "speed" : 2,
        "cooldown_time" : 0,
        "hording_time" : 0,
    },'ghost' : {
        "size" : [50, 70],
        0 : {"frame" : 8, "bottom" : 62, "width" : 82, "height" : 62},     #idle
        1 : {"frame" : 6, "bottom" : 0, "width" : 82, "height" : 52},      #run
        2 : None,
        3 : None,
        "speed" : 6,
        "cooldown_time" : 0,
        "hording_time" : 0,
    },'pikachu' : {
        "size" : [50, 70],
        0 : {"frame" : 4, "bottom" : 101, "width" : 60, "height" : 44},     #idle
        1 : {"frame" : 4, "bottom" : 59, "width" : 60, "height" : 32},      #run
        2 : {"frame" : 3, "bottom" : 0, "width" : 60, "height" : 49},      #run
        3 : None,
        "speed" : 4,
        "cooldown_time" : 0,
        "hording_time" : 0,
    }
}

class Character:
    def __init__(self, name, x, y):
        self.image = load_image('res/{}.png'.format(name))
        self.character = characters[name]

        self.x = x
        self.y = y
        self.speed = self.character['speed']
        self.dirX = 0
        self.dirY = 0
        self.state = 0

        self.frame = 0
        self.frameNum = 0
        self.frameSize = (0, 0, 0, 0)
        self.set_animation()

        self.available_skill = True
        self.active_skill_time = 0

    def set_animation(self):
        if self.character[self.state] != None:
            self.frameNum = self.character[self.state]['frame']
            self.frameSize = (
                self.character[self.state]['width'],
                self.character[self.state]['bottom'],
                self.character[self.state]['width'],
                self.character[self.state]['height'],
            )

    def draw_character(self):
        self.set_animation()
        self.image.clip_draw(8+self.frameSize[0]*self.frame, self.frameSize[1], self.frameSize[2], self.frameSize[3], self.x, self.y, 50, 80)

    def update(self):
        self.frame = (self.frame + 1) % self.frameNum

        self.skill(time.time())

        self.x += (self.dirX) * self.speed
        self.y += (self.dirY) * self.speed
        if self.y >= 520:
            self.y = 519
        elif self.y <= 90:
            self.y = 91

    def skill(self ,eTime):
        if eTime - self.active_skill_time >= self.character['cooldown_time']:
            self.available_skill = True
            self.active_skill_time = 0
        
        if not self.available_skill: # 스킬 사용 중
            if eTime - self.active_skill_time <= self.character['hording_time']:
                self.speed = 5
                self.state = 3
        
        