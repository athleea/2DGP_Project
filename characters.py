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
    },
    'sonic' : {
        "size" : [50, 70],
        0 : {"frame" : 4, "bottom" : 174, "width" : 30, "height" : 40},     #idle
        1 : {"frame" : 8, "bottom" : 126, "width" : 42, "height" : 38},      #run
        2 : {"frame" : 2, "bottom" : 71, "width" : 40, "height" : 45},       #sturn
        3 : {"frame" : 5, "bottom" : 37, "width" : 34, "height" : 34},
        4 : {"frame" : 6, "bottom" : 0, "width" : 31, "height" : 27},
        "speed" : 1,
        "cooldown_time" : 10,
        "hording_time" : 3,
    }
}

class Character:
    def __init__(self, name, x, y):
        self.image = load_image('res/{}.png'.format(name))
        self.character = characters[name]

        self.x = x
        self.y = y
        self.speed = 0
        self.dir = 0
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

    def draw(self):
        self.set_animation()
        self.image.clip_draw(8+self.frameSize[0]*self.frame, self.frameSize[1], self.frameSize[2], self.frameSize[3], self.x, self.y, 50, 70)

    def update(self):
        self.frame = (self.frame + 1) % self.frameNum

        self.skill(time.time())

        self.x += self.speed
        self.y += self.dir * self.speed
        if self.y >= 520:
            self.y -= self.speed
        elif self.y <= 80:
            self.y += self.speed

    def skill(self ,eTime):
        if eTime - self.active_skill_time >= self.character['cooldown_time']:
            self.available_skill = True
            self.active_skill_time = 0
        
        if not self.available_skill: # 스킬 사용 중
            if eTime - self.active_skill_time <= self.character['hording_time']:
                self.speed = 5
                self.state = 3
        else: # 스킬 미 사용 중
            self.speed = self.character['speed']
            self.state = 1

    def move(self, direction):
        self.state = 1
        self.speed = self.character['speed']
        self.dir += direction
        
    def handle_events(self):
        for event in get_events():
            if event.type == SDL_QUIT:
                pass
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    pass
                elif event.key == SDLK_UP:
                    self.move(1)
                elif event.key == SDLK_DOWN:
                    self.move(-1)
                elif event.key == SDLK_r:
                    if self.available_skill:
                        self.available_skill = False
                        self.active_skill_time = time.time()
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_UP:
                    self.dir -= 1
                elif event.key == SDLK_DOWN:
                    self.dir += 1
                elif event.key == SDLK_r:
                    pass