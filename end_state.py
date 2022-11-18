from pico2d import *

import game_framework
import play_state
import lobby_state
import game_world

image = None

def enter():
    global image
    image = load_image('res/finish.png')


def exit():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONUP:
            if 470 <= event.y <= 545:
                if 45 <= event.x <= 315:
                    play_state.game_restart = True
                    game_framework.pop_state()
                elif 485 <= event.x <=755:
                    play_state.lobby_start = True
                    game_framework.pop_state()

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
