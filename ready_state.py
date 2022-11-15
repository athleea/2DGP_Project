import game_framework
import play_state
from pico2d import *

count = None
countdown = 3
enter_time = 0.0
end_time = 0.0


def enter():
    global count, enter_time, end_time
    count = load_font('res/ENCR10B.TTF', 30)
    enter_time = game_framework.cur_time


def exit():
    global count
    del count


def update():
    global count, enter_time, end_time, countdown
    if game_framework.cur_time < enter_time + 1:
        countdown = 3
    elif game_framework.cur_time < enter_time + 2:
        countdown = 2
    elif game_framework.cur_time < enter_time + 3:
        countdown = 1
    elif game_framework.cur_time >= enter_time + 3:
        play_state.gamestart = True
        game_framework.pop_state()


def draw():
    global countdown
    clear_canvas()
    play_state.draw_world()
    count.draw(400, 300, f'{countdown}')
    update_canvas()


def handle_events():
    events = get_events()
