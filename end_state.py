from pico2d import *

import game_framework
import play_state
from player import Player

image = None
winner_font = None

def enter():
    global image, winner_font
    image = load_image('res/finish.png')
    winner_font = load_font('res/NanumGothic.TTF', 100)


def exit():
    global image, winner_font
    del image, winner_font

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
    if type(play_state.winner) is Player:
        winner_font.draw(300, 300, f'Win!', (255, 255, 0))
    else:
        winner_font.draw(300, 300, f'Lose..', (255, 255, 0))
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
