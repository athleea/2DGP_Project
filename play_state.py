import game_framework
from map_object import Background
import title_state

from pico2d import *
from character_object import *

player = None
background = None
running = None

def enter():
    global player, background, running
    player = Character('sonic', 50, 90)
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
    player.draw()
    update_canvas()

def handle_events():
        for event in get_events():
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    game_framework.change_state(title_state)
                elif event.key == SDLK_UP:
                    player.move(1)
                elif event.key == SDLK_DOWN:
                    player.move(-1)
                elif event.key == SDLK_r:
                    if player.available_skill:
                        player.available_skill = False
                        player.active_skill_time = time.time()
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_UP:
                    player.dir -= 1
                elif event.key == SDLK_DOWN:
                    player.dir += 1
                elif event.key == SDLK_r:
                    pass
        delay(0.05)
            
    