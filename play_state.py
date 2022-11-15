import game_framework
import lobby_state
import game_world
import ready_state

from player import *
from background import Background
from timer import Timer
from ai import AI

gamestart = None
player = None
ai = None
raceTimer = None
background = None
difficulty = 0


def enter():
    global player, background, ai, gamestart, raceTimer

    gamestart = False

    player = Player()
    background = Background()
    raceTimer = Timer()
    ai = [AI(y=480), AI(y=400), AI(y=300), AI(y=200)]

    game_world.add_object(player, 0)
    game_world.add_object(ai, 1)
    game_world.add_object(timer, 1)
    game_world.add_object(background, 2)


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



def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    background.draw()
    raceTimer.draw()
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
