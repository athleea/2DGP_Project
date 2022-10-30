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
        3 : {"frame" : 6, "bottom" : 0, "width" : 32, "height" : 27},       #skill
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
    },'kirby' : {
        "size" : [50, 70],
        0 : {"frame" : 6, "bottom" : 85, "width" : 50, "height" : 40},     #idle
        1 : {"frame" : 4, "bottom" : 45, "width" : 50, "height" : 40},      #run
        2 : {"frame" : 4, "bottom" : 0, "width" : 50, "height" : 45},       #sturn
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
        0 : {"frame" : 8, "bottom" : 65, "width" : 75, "height" : 63},     #idle
        1 : {"frame" : 6, "bottom" : 0, "width" : 75, "height" : 55},      #run
        2 : None,
        3 : None,
        "speed" : 6,
        "cooldown_time" : 0,
        "hording_time" : 0,
    },'pikachu' : {
        "size" : [50, 70],
        0 : {"frame" : 4, "bottom" : 85, "width" : 60, "height" : 45},     #idle
        1 : {"frame" : 4, "bottom" : 50, "width" : 60, "height" : 35},      #run
        2 : {"frame" : 3, "bottom" : 0, "width" : 60, "height" : 50},      #run
        3 : None,
        "speed" : 4,
        "cooldown_time" : 0,
        "hording_time" : 0,
    },'among' : {
        "size" : [50, 70],
        0 : {"frame" : 1, "bottom" : 110, "width" : 30, "height" : 25},     
        1 : {"frame" : 4, "bottom" : 75, "width" : 30, "height" : 25},      
        2 : {"frame" : 4, "bottom" : 35, "width" : 30, "height" : 30},      
        3 : {"frame" : 4, "bottom" : 0, "width" : 30, "height" : 25},      
        "speed" : 4,
        "cooldown_time" : 0,
        "hording_time" : 0,
    },'dog' : {
        "size" : [50, 70],
        0 : {"frame" : 2, "bottom" : 150, "width" : 100, "height" : 45},     
        1 : {"frame" : 7, "bottom" : 85, "width" : 100, "height" : 65},      
        2 : {"frame" : 6, "bottom" : 0, "width" : 100, "height" : 85},      
        3 : None,
        "speed" : 4,
        "cooldown_time" : 0,
        "hording_time" : 0,
    },'human' : {
        "size" : [50, 70],
        0 : {"frame" : 1, "bottom" : 158, "width" : 38, "height" : 42},     #idle
        1 : {"frame" : 4, "bottom" : 108, "width" : 38, "height" : 40},      #run
        2 : {"frame" : 2, "bottom" : 52, "width" : 38, "height" : 46},      #sturn
        3 : {"frame" : 3, "bottom" : 0, "width" : 38, "height" : 42},      #skill
        "speed" : 4,
        "cooldown_time" : 0,
        "hording_time" : 0,
    },'icarus' : {
        "size" : [50, 70],
        0 : {"frame" : 4, "bottom" : 204, "width" : 65, "height" : 60},     #idle
        1 : {"frame" : 6, "bottom" : 144, "width" : 65, "height" : 60},      #run
        2 : {"frame" : 8, "bottom" : 84, "width" : 65, "height" : 60},      #run
        3 : {"frame" : 4, "bottom" : 24, "width" : 65, "height" : 60},
        "speed" : 4,
        "cooldown_time" : 0,
        "hording_time" : 0,
    },'ninja' : {
        "size" : [50, 70],
        0 : {"frame" : 4, "bottom" : 210, "width" : 60, "height" : 75},     #idle
        1 : {"frame" : 6, "bottom" : 145, "width" : 60, "height" : 65},      #run
        2 : {"frame" : 4, "bottom" : 70, "width" : 80, "height" : 75},      #run
        3 : {"frame" : 2, "bottom" : 0, "width" : 60, "height" : 70},
        "speed" : 4,
        "cooldown_time" : 0,
        "hording_time" : 0,
    },'witch' : {
        "size" : [50, 70],
        0 : {"frame" : 5, "bottom" : 305, "width" : 100, "height" : 95},     #idle
        1 : {"frame" : 2, "bottom" : 205, "width" : 100, "height" : 100},      #run
        2 : {"frame" : 5, "bottom" : 120, "width" : 110, "height" : 85},      #run
        3 : {"frame" : 4, "bottom" : 0, "width" : 100, "height" : 120},
        "speed" : 4,
        "cooldown_time" : 0,
        "hording_time" : 0,
    },'zombie' : {
        "size" : [50, 70],
        0 : {"frame" : 4, "bottom" : 145, "width" : 90, "height" : 75},     #idle
        1 : {"frame" : 5, "bottom" : 70, "width" : 90, "height" : 75},      #run
        2 : {"frame" : 8, "bottom" : 0, "width" : 90, "height" : 70},      #run
        3 : None,
        "speed" : 2,
        "cooldown_time" : 0,
        "hording_time" : 0,
    },
    
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
        self.image.clip_draw(self.frameSize[0]*self.frame, self.frameSize[1], self.frameSize[2], self.frameSize[3], self.x, self.y, 50, 80)
        delay(0.5)

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

    def handle_events(self, event):
        if event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_UP:
                    self.dirY += 1
                    self.state = 1
                case pico2d.SDLK_DOWN:
                    self.dirY -= 1
                    self.state = 1
                case pico2d.SDLK_RIGHT:
                    self.dirX += 1
                    self.state = 1
                case pico2d.SDLK_r:
                    self.state = 3
                    pass
                case pico2d.SDLK_d: #character sprite test
                    self.state = 2
        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_UP:
                    self.dirY -= 1
                    self.state = 0
                case pico2d.SDLK_DOWN:
                    self.dirY += 1
                    self.state = 0
                case pico2d.SDLK_RIGHT:
                    self.dirX -= 1
                    self.state = 0
                case pico2d.SDLK_r:
                    self.state = 0
                case pico2d.SDLK_d:
                    self.state = 0
                    pass
        
        