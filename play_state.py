import game_framework
from map_object import Background
import lobby_state

from pico2d import *
from character_object import *

import random

player = None
background = None
running = None
difficulty = 0

def enter():
    global player, background, running
    #print(type(random.choice(characters.keys())))
    player = Character('zombie', 30, 90)
    background = Background()
    running = True

def exit():
    global player, background
    del background

def update():
    player.update()

def draw():
    clear_canvas()
    background.draw()
    player.draw_character()
    update_canvas()
    delay(0.05)

def handle_events():
        for event in get_events():
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(lobby_state)
            else:
                player.handle_events(event)
        
            
    