import game_framework
import lobby_state
import game_world
import ready_state

from player import *
from stone import Stone
from background import Background
from lines import *
from timer import Timer
from ai import AI
from map import *

gamestart = None
player = None
ai = []
raceTimer = None
bg = None
startLine = None
transformLine = []
finishLine = None
map = None
pin = []
difficulty = 0
stones = []

observer = None

def enter():
    global player, bg, ai, gamestart, raceTimer, startLine, finishLine, transformLine, map, observer, pin, stones, mapX
    gamestart = False

    observer = [[],[],[],[],[]]
    map = Map()
    pin = [Pin(i) for i in range(5)]
    raceTimer = Timer()

    player = Player()
    ai = [AI(y=480), AI(y=400), AI(y=300), AI(y=200)]

    stones = [Stone() for i in range(5)]

    bg = Background()
    startLine = StartLine()
    transformLine = [TransformLine(x=1500*i) for i in range(1,5+1)] 
    finishLine = FinishLine()

    for i in range(4):
        observer[i] = ai[i].get_pos()
    observer[4] = player.get_pos()

    game_world.add_object(player, 2)
    game_world.add_objects(ai, 2)
    game_world.add_objects(stones, 2)
    game_world.add_object(raceTimer, 1)
    game_world.add_object(map, 1)
    game_world.add_objects(pin, 1)
    game_world.add_object(bg, 0)
    game_world.add_object(startLine, 1)
    game_world.add_object(finishLine, 1)
    game_world.add_objects(transformLine, 1)

    game_world.add_collision_pairs(player, stones, 'player:stone')
    game_world.add_collision_pairs(ai, stones, 'ai:stone')
    game_world.add_collision_pairs(player, transformLine, 'player:t_line')
    game_world.add_collision_pairs(ai, transformLine, 'ai:t_line')

def exit():
    game_world.clear()


def update():
    if not play_state.gamestart:
        game_framework.push_state(ready_state)
    else:
        for game_object in game_world.all_objects():
            game_object.update()
        
        for i in range(4):
            observer[i] = ai[i].get_pos()
        observer[4] = player.get_pos()

        for a, b, group in game_world.all_collision_pairs():
            if collide(a, b):
                a.handle_collision(b, group)
                b.handle_collision(a, group)

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
            player.handle_events(event)

def pause():
    pass

def resume():
    pass

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True