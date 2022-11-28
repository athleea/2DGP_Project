import ready_state
import end_state
import lobby_state
import play_state
import game_world
import server

from player import *
from stone import Stone
from background import Background
from timer import Timer
from ai import AI
from minimap import *
from pin import Pin
from transform_line import TransformLine
from finish_line import FinishLine
from start_line import StartLine

game_start = None
game_over = None
game_restart = None
lobby_start = None
difficulty = 0

player = None
ai = []
stones = []

bg = None
race_timer = None
start_line = None
transform_line = []
finish_line = None
mini_map = None
pins = []

pos_observer = None


def enter():
    global start_line, transform_line, finish_line, mini_map, pins, race_timer
    global stones, pos_observer
    global game_start, game_over, game_restart, lobby_start

    game_start = False
    game_over = False
    game_restart = False
    lobby_start = False

    pos_observer = [[], [], [], [], []]
    mini_map = MiniMap()
    pins = [Pin(i) for i in range(5)]
    race_timer = Timer()

    server.player = Player()
    server.ai = [AI(y=90*(i+2)) for i in range(4)]

    stones = [Stone() for i in range(5)]

    server.background = Background()
    start_line = StartLine()
    transform_line = [TransformLine(x=1500*i) for i in range(1,5+1)]

    finish_line = FinishLine()

    for i in range(4):
        pos_observer[i] = server.ai[i].get_pos()
    pos_observer[4] = server.player.get_pos()

    game_world.add_objects(stones, 2)
    game_world.add_objects(server.ai, 2)
    game_world.add_object(server.player, 2)

    game_world.add_object(race_timer, 1)
    game_world.add_object(mini_map, 1)
    game_world.add_objects(pins, 1)
    game_world.add_object(start_line, 1)
    game_world.add_object(finish_line, 1)
    game_world.add_objects(transform_line, 1)

    game_world.add_object(server.background, 0)

    game_world.add_collision_pairs(server.player, stones, 'character:stone')
    game_world.add_collision_pairs(server.ai, stones, 'character:stone')
    game_world.add_collision_pairs(server.player, transform_line, 'character:transform_line')
    game_world.add_collision_pairs(server.ai, transform_line, 'character:transform_line')
    game_world.add_collision_pairs(server.player, finish_line, 'character:finish_line')
    game_world.add_collision_pairs(server.ai, finish_line, 'character:finish_line')


def exit():
    global game_start, game_over, game_restart, lobby_start
    del game_start, game_over, game_restart, lobby_start
    game_world.clear()
    game_world.collision_group.clear()


def update():
    if game_start is False:
        game_framework.push_state(ready_state)
    elif game_over is True:
        game_framework.push_state(end_state)
    else:
        global pos_observer
        for game_object in game_world.all_objects():
            game_object.update()

        for a, b, group in game_world.all_collision_pairs():
            if collide(a, b):
                a.handle_collision(b, group)
                b.handle_collision(a, group)

        for i in range(4):
            pos_observer[i] = server.ai[i].get_pos()
        pos_observer[4] = server.player.get_pos()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(lobby_state)
        else:
            server.player.handle_events(event)


def pause():
    pass


def resume():
    if game_restart is True:
        game_world.clear()
        game_framework.change_state(play_state)
    if lobby_start is True:
        game_framework.change_state(lobby_state)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
