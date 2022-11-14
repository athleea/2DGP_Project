import game_framework
import lobby_state
import game_world

from player import *
from background import Background

player = None
ai = None;
background = None
difficulty = 0

def enter():
    global player, background
    
    player = Player()
    background = Background()

    game_world.add_object(player, 0)
    game_world.add_object(background, 1)

def exit():
    game_world.clear()

def update():
    player.update()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    background.draw()
    player.draw()

def handle_events():
        for event in get_events():
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(lobby_state)
            else:
                player.handle_events(event)

    