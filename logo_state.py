import game_framework
import lobby_state
from pico2d import *

image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('res/logo.png')


def exit():
    global image
    del image


def update():
    global logo_time

    if logo_time > 1.0:
        logo_time = 0
        game_framework.change_state(lobby_state)
    delay(0.01)
    logo_time += 0.01


def draw():
    clear_canvas()
    image.draw(400, 300, 800, 600)
    update_canvas()


def handle_events():
    events = get_events()
