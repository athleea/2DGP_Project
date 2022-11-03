import game_framework
import lobby_state

from pico2d import *
from character import *
from map_object import *

player = None
background = None
difficulty = 0

def enter():
    global player, background, running
    
    player = Character()
    background = Background()

def exit():
    global player, background
    del background

def update():
    player.update()

def draw():
    clear_canvas()
    background.draw()
    player.draw()
    update_canvas()

def handle_events():
        for event in get_events():
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(lobby_state)
            else:
                player.handle_events(event)

    