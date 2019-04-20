#! /usr/bin/env python3
# coding: utf-8


'''The dosplay module handles the display of the graphbic interface
It requires both a character and a game controller to work properly'''


import pygame


class DisplayController:
    '''handles sprites loading from ressources folder
    also displays them in the window, based on their position on the grid'''

    WINDOW_WIDTH = 750
    WINDOW_HEIGHT = 800
    TILE_LENGTH = 50

    DISPLAY_WINDOW = None

    TILE_SPRITE = pygame.image.load("ressources/tile.png")
    CHARACTER_SPRITE = pygame.image.load("ressources/character.png")
    WARDEN_SPRITE = pygame.image.load("ressources/warden.png")
    NEEDLE_SPRITE = pygame.image.load("ressources/needle.png")
    PIPE_SPRITE = pygame.image.load("ressources/pipe.png")
    ETHER_SPRITE = pygame.image.load("ressources/ether.png")
    WALL_SPRITE = pygame.image.load("ressources/wall.png")
    VICTORY_SCREEN = pygame.image.load("ressources/victory.jpg")
    DEFEAT_SCREEN = pygame.image.load("ressources/defeat.jpg")
    ITEM_TRACKER = pygame.image.load("ressources/item_tracker.png")

    CHARACTER = None
    GAME_CONTROLLER = None

    @classmethod
    def initialize_display(cls):
        '''This method is called once, at the beginning of the script,
        to blit permanent sprites (that are walls and item tracker)'''

        cls.DISPLAY_WINDOW = pygame.display.set_mode(
                            (cls.WINDOW_WIDTH, cls.WINDOW_HEIGHT))

        for y in range(0, int((cls.WINDOW_HEIGHT / cls.TILE_LENGTH)) - 1):

            for x in range(0, int(cls.WINDOW_WIDTH / cls.TILE_LENGTH)):

                cls.DISPLAY_WINDOW.blit(cls.WALL_SPRITE, 
                                    (x * cls.TILE_LENGTH, y * cls.TILE_LENGTH))

        cls.DISPLAY_WINDOW.blit(cls.ITEM_TRACKER, 
                                (0, cls.WINDOW_HEIGHT - cls.TILE_LENGTH))

        cls.refresh_display()

    @classmethod
    def refresh_display(cls):
        '''The method is called after each action (i.e when the character moves).
        It displays game over screen if needed ; otherwise, it will blit new
        tile sprites, remaining items, warden and character, and finally
        updates the item tracker with item collected so far.'''

        row_length = cls.WINDOW_WIDTH / cls.TILE_LENGTH

        if cls.GAME_CONTROLLER.GAME_STATE == "Victory":
            cls.DISPLAY_WINDOW.blit(cls.VICTORY_SCREEN, (0, 0))

        elif cls.GAME_CONTROLLER.GAME_STATE == "Defeat":
            cls.DISPLAY_WINDOW.blit(cls.DEFEAT_SCREEN, (0, 0))

        else:

            # floor sprites

            for position in cls.GAME_CONTROLLER.SQUARE_SET + list(
                            cls.GAME_CONTROLLER.SPECIAL_SQUARES.keys()):

                position_x = int(position % row_length) * cls.TILE_LENGTH
                position_y = int(position / row_length) * cls.TILE_LENGTH

                cls.DISPLAY_WINDOW.blit(cls.TILE_SPRITE,
                                       (position_x, position_y))

                # items sprites

                if position in cls.GAME_CONTROLLER.SPECIAL_SQUARES:

                    if cls.GAME_CONTROLLER.SPECIAL_SQUARES[position] == "warden":
                        cls.DISPLAY_WINDOW.blit(cls.WARDEN_SPRITE,
                                               (position_x, position_y))

                    elif cls.GAME_CONTROLLER.SPECIAL_SQUARES[position] == "pipe":
                        cls.DISPLAY_WINDOW.blit(cls.PIPE_SPRITE, 
                                               (position_x, position_y))

                    elif cls.GAME_CONTROLLER.SPECIAL_SQUARES[position] == "needle":
                        cls.DISPLAY_WINDOW.blit(cls.NEEDLE_SPRITE,
                                               (position_x, position_y))

                    elif cls.GAME_CONTROLLER.SPECIAL_SQUARES[position] == "ether":
                        cls.DISPLAY_WINDOW.blit(cls.ETHER_SPRITE,
                                               (position_x, position_y))

            # character's sprite

            cls.DISPLAY_WINDOW.blit(cls.CHARACTER_SPRITE,
                       (int(cls.CHARACTER.position % row_length) * cls.TILE_LENGTH,
                       int(cls.CHARACTER.position / row_length) * cls.TILE_LENGTH))

            # collected items

            tracker_height = cls.WINDOW_HEIGHT - cls.TILE_LENGTH

            for count, item in enumerate(cls.CHARACTER.items, 0):
                if item == "needle":
                    cls.DISPLAY_WINDOW.blit(cls.NEEDLE_SPRITE,
                                ((5 + count) * cls.TILE_LENGTH, tracker_height))
                elif item == "pipe":
                    cls.DISPLAY_WINDOW.blit(cls.PIPE_SPRITE,
                                ((5 + count) * cls.TILE_LENGTH, tracker_height))
                elif item == "ether":
                    cls.DISPLAY_WINDOW.blit(cls.ETHER_SPRITE,
                                ((5 + count) * cls.TILE_LENGTH, tracker_height))

        pygame.display.flip()
