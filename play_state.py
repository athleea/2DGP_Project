import game_framework
import lobby_state
import game_world
import ready_state
import lines

from player import *
from background import Background
from lines import *
from timer import Timer
from ai import AI
from map import *

gamestart = None
player = None
ai = None
raceTimer = None
background = None
startLine = None
transformLine = None
finishLine = None
map = None
pin = None
difficulty = 0

observer = None

def enter():
    global player, background, ai, gamestart, raceTimer, startLine, finishLine, transformLine, map, observer, pin
    gamestart = False

    observer = [[],[],[],[],[]]
    map = Map()
    pin = [Pin(i) for i in range(5)]
    raceTimer = Timer()

    player = Player()
    ai = [AI(y=480), AI(y=400), AI(y=300), AI(y=200)]


    background = Background()
    startLine = StartLine()
    transformLine = [TransformLine(x=1500), TransformLine(x=3000), TransformLine(x=4500), TransformLine(x=6000), TransformLine(x=7500), TransformLine(x=9000)]
    finishLine = FinishLine()




    game_world.add_object(player, 0)
    game_world.add_object(ai, 1)
    game_world.add_object(timer, 1)
    game_world.add_object(map, 1)
    game_world.add_object(pin, 1)
    game_world.add_object(background, 2)
    game_world.add_object(startLine, 2)
    game_world.add_object(finishLine, 2)
    game_world.add_object(transformLine, 2)


def exit():
    game_world.clear()


def update():
    if not play_state.gamestart:
        game_framework.push_state(ready_state)
    else:
        raceTimer.update()
        player.update()
        for a in ai:
            a.update()
        for i in range(4):
            observer[i] = [ai[i].x, ai[i].y]
        observer[4] = [player.x, player.y]

        for p in pin:
            p.update()





def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    background.draw()
    startLine.draw()
    finishLine.draw()
    for tf in transformLine:
        tf.draw()
    raceTimer.draw()
    map.draw()

    for p in pin:
        p.draw()

    for a in ai:
        a.draw()
    player.draw()



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
