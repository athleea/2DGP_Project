from pico2d import *

import game_framework
import play_state

image = None
difficulty = 0
d_image = []
def enter():
    global image, d_image
    image = load_image('res/title.png')
    d_image = [ load_image('res/easy.png'), load_image('res/normal.png'), load_image('res/hard.png') ]
    

def exit():
    global image, d_image, difficulty
    del image
    del d_image
    del difficulty
    

def handle_events():
    global difficulty
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONUP:
            if event.x >= 610:
                if event.y >= 340 and event.y <= 370:
                    game_framework.change_state(play_state)
                elif event.y >= 470 and event.y <= 500:
                    game_framework.quit()
            if event.y >= 420 and event.y <= 450:
                if event.x >= 580 and event.x <= 630:
                    difficulty, play_state.difficulty = 0, 0
                    print(difficulty)
                elif event.x >= 640 and event.x <= 690:
                    difficulty, play_state.difficulty = 1, 1
                    print(difficulty)
                elif event.x >= 700 and event.x <= 780:
                    difficulty, play_state.difficulty = 2, 2
                    print(difficulty)
                


def draw():
    clear_canvas()
    image.draw(400,300)
    d_image[difficulty].draw(690, 165)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass