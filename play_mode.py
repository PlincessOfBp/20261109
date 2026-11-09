from pico2d import *
import game_framework
import game_world
import pause_mode
import title_mode
import item_mode
from boy import Boy
from grass import Grass

pause_started_at = 0.0
selected_ball = 1


def handle_events():
    event_list = get_events()
    for event in event_list:
        if handle_event(event):
            return


def handle_event(event):
    if event.type == SDL_QUIT:
        game_framework.quit()
        return True
    if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
        game_framework.change_mode(title_mode)
        return True
    if event.type == SDL_KEYDOWN and event.key == SDLK_p:
        game_framework.push_mode(pause_mode)
        return True
    if event.type == SDL_KEYDOWN and event.key == SDLK_i:
        game_framework.push_mode(item_mode, pause_current=False)
        return True
    boy.handle_event(event)
    return False


def init():
    global boy
    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)

def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    update_canvas()


def render_scene():
    clear_canvas()
    game_world.render()


def finish():
    game_world.clear()

def pause():
    global pause_started_at
    pause_started_at = get_time()

def resume():
    boy.idle_started_at += get_time() - pause_started_at
