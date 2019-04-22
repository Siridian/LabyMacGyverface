#! /usr/bin/env python3
# coding: utf-8


'''This is the main module. It contains the main function
that enables gameplay loop. It also initializes display window.
'''


import pygame
from pygame.locals import QUIT, KEYDOWN, K_RIGHT, K_LEFT, K_DOWN, K_UP

from controllers.game_controller import GameController as gc
from controllers.character_controller import Macgyver
from controllers.display_controller import DisplayController as dc


def main():
    '''Initializes the grid, player's agent, and handles gameplay loop'''

    pygame.init()

    gc.initialize_squares()
    character = Macgyver(gc.START_SQUARE_ID, gc)
    dc.CHARACTER = character
    dc.GAME_CONTROLLER = gc

    dc.initialize_display()

    while gc.GAME_STATE == "Running":
        for event in pygame.event.get():
            if event.type == QUIT:
                gc.GAME_STATE = "Terminated"

            row_length = dc.WINDOW_WIDTH / dc.TILE_LENGTH

            if (event.type == KEYDOWN and
                    event.key in (K_LEFT, K_UP, K_RIGHT, K_DOWN)):

                if event.key == K_LEFT:
                    if character.position % row_length != 0: 
                        character.move(-1)

                elif event.key == K_UP:
                    character.move(int(- row_length))

                elif event.key == K_RIGHT:
                    if character.position % row_length != row_length -1:
                        character.move(1)

                elif event.key == K_DOWN:
                    character.move(int(row_length))

                character.touch_square()
                dc.refresh_display()

    while gc.GAME_STATE in ("Victory", "Defeat"):
        for event in pygame.event.get():
            if event.type == QUIT:
                gc.GAME_STATE = "Terminated"


if __name__ == "__main__":
    main()
