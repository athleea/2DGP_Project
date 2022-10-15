from pico2d import *
import random
import characters


playing = True

class Character:
    def __init__(self, name, x, y):
        self.image = load_image('res/{}.png'.format(name))
        self.character = characters.characters[name]

        self.x = x
        self.y = y
        self.speed = 0
        self.dir = 0
        self.state = 0

        self.frame = 0
        self.maxFrame = self.character[self.state]['frame']
        self.frameSize = (
            self.character[self.state]['width'],
            self.character[self.state]['bottom'],
            self.character[self.state]['width'],
            self.character[self.state]['height'])

    def set_animation(self):
        if self.character[self.state] != None:
            self.maxFrame = self.character[self.state]['frame']
            self.frameSize = (
                self.character[self.state]['width'],
                self.character[self.state]['bottom'],
                self.character[self.state]['width'],
                self.character[self.state]['height'],
            )

    def draw(self):
        self.set_animation()
        self.image.clip_draw(8+self.frameSize[0]*self.frame, self.frameSize[1], self.frameSize[2], self.frameSize[3], self.x, self.y,self.character['size'][0], self.character['size'][1])

    def update(self):
        self.frame = (self.frame + 1) % self.maxFrame
        self.x += self.speed
        self.y += self.dir * self.speed

    def handle_events(self):
        global playing
        for event in get_events():
            if event.type == SDL_QUIT:
                playing = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    playing = False
                elif event.key == SDLK_UP:
                    self.speed = self.character['speed']
                    self.dir += 1
                    self.state = 1
                elif event.key == SDLK_DOWN:
                    self.speed = self.character['speed']
                    self.dir -= 1
                    self.state = 1
                elif event.key == SDLK_r:
                    self.state = 3

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_UP:
                    self.dir -= 1
                elif event.key == SDLK_DOWN:
                    self.dir += 1
                elif event.key == SDLK_r:
                    pass

    
    def changeCharacter(self):
        characterList = list(characters.characters.keys())
        index = random.randint(0, len(characterList)-1)
        self.character = characters.characters[characterList[index]]
        

playing = True

open_canvas()

char = Character('sonic', 30, 90)
map = load_image('res/background.png')

MAP_WIDTH = 800
MAP_HEIGHT = 600

while playing:
    clear_canvas()
    map.draw(MAP_WIDTH // 2,MAP_HEIGHT // 2)
    char.handle_events()
    if char.y >= 520:
        char.y -= char.speed
    elif char.y <= 80:
        char.y += char.speed
    char.update()
    char.draw()
    update_canvas()
    delay(0.05)

close_canvas()
