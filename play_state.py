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
    player = Character('Patrick_Star', 30, 90)
    background = Background()
    running = True

def exit():
    global player, background
    del player
    del background

def update():
    player.update()

def draw():
    clear_canvas()
    background.draw()
    player.draw_character()
    update_canvas()

def handle_events():
        for event in get_events():
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    game_framework.change_state(lobby_state)
                elif event.key == SDLK_RIGHT:
                    player.dirX += 1
                    player.state = 1
                elif event.key == SDLK_UP:
                    player.dirY += 1
                    player.state = 1
                elif event.key == SDLK_DOWN:
                    player.dirY -= 1
                    player.state = 1
                elif event.key == SDLK_r:
                    if player.available_skill:
                        player.available_skill = False
                        player.active_skill_time = time.time()
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_UP:
                    player.dirY -= 1
                    player.state = 0
                elif event.key == SDLK_DOWN:
                    player.state = 0
                    player.dirY += 1
                elif event.key == SDLK_RIGHT:
                    player.state = 0
                    player.dirX -= 1
                elif event.key == SDLK_r:
                    pass
        delay(0.05)
            
    