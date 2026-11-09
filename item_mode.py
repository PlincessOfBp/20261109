import game_framework
import play_mode
from ball import Ball
from pico2d import get_events, load_image, update_canvas
from sdl2 import (SDL_KEYDOWN, SDL_QUIT, SDLK_0, SDLK_1, SDLK_2, SDLK_ESCAPE,
                  SDLK_i)

image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    del image


def update():
    play_mode.update()


def render():
    play_mode.render_scene()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return

        if event.type == SDL_KEYDOWN:
            if event.key in (SDLK_ESCAPE, SDLK_i):
                game_framework.pop_mode(resume_current=False)
                return
            if event.key in (SDLK_0, SDLK_1, SDLK_2):
                Ball.selected_size = event.key - SDLK_0
                game_framework.pop_mode(resume_current=False)
                return

        if play_mode.handle_event(event):
            return
