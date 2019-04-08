#! /usr/bin/env python3
# coding: utf-8


'''This is the main module. It contains the main function
that enables gameplay loop. It also initializes display window.
'''

import random
import pygame
from pygame.locals import *

from game_controller import GameController
from display_controller import DisplayController
from character_controller import Macgyver


def main():
    '''Initializes the grid, player's agent, and handles gameplay loop'''

    game_controller = GameController()
    display_controller = DisplayController(game_controller)

    """
    pygame.init() #enables sprite initialization during display_controller class declaration
    game_window = pygame.display.set_mode((750, 750))
    display_controller.WINDOW = game_window
    """

    game_controller.initialize_squares()

    display_controller.initialize_display()   
    display_controller.refresh_display()


    character = Macgyver(game_controller.start_square_position, game_controller, display_controller)

    while game_controller.RUNNING:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_controller.RUNNING = False

            if (event.type == KEYDOWN and
                    event.key in (K_LEFT, K_UP, K_RIGHT, K_DOWN)):

                character.current_square.content = 0

                if event.key == K_LEFT:
                    character.move_left()

                elif event.key == K_UP:
                    character.move_up()

                elif event.key == K_RIGHT:
                    character.move_right()

                elif event.key == K_DOWN:
                    character.move_down()

                character.touch_square()
                character.current_square.content = 6
                display_controller.refresh_display()

    while game_controller.GAME_OVER:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_controller.GAME_OVER = False

if __name__ == "__main__":
    main()
