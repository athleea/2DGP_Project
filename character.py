from pico2d import *
from characters import *

playing = True

open_canvas()

char = Character('Patrick_Star', 30, 90)
map = load_image('res/background.png')

MAP_WIDTH = 800
MAP_HEIGHT = 600

while playing:
    clear_canvas()
    map.draw(MAP_WIDTH // 2,MAP_HEIGHT // 2)
    char.handle_events()
    char.update()
    char.draw()
    update_canvas()
    delay(0.05)

close_canvas()