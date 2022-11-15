import pico2d
import game_framework
import logo_state
import play_state

start_state = logo_state

pico2d.open_canvas()
game_framework.run(play_state)
pico2d.close_canvas()
