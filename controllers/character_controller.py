#! /usr/bin/env python3
# coding: utf-8


'''The character module handles the event triggerd by the player inputs
It requires a game controller to work properly'''


class Macgyver:
    '''The MacGyver class represents the player-controlled character
    It handles movement, item pick-up, item storage, and game over'''

    def __init__(self, start_position, game_controller):
        '''Constructor spawns the character at a given square on the grid
        and links it to the specified game controller'''
        self.position = start_position
        self.items = []
        self.gc = game_controller

    def touch_square(self):
        '''Triggers various events when the character enters an occupied square
        Items will be added to inventory
        Encounter with the warden results in either victory or defeat'''

        if self.position in self.gc.SPECIAL_SQUARES:
            if self.gc.SPECIAL_SQUARES[self.position] == "warden":

                if len(self.items) == len(self.gc.ITEM_LIST):
                    self.gc.GAME_STATE = "Victory"

                else:
                    self.gc.GAME_STATE = "Defeat"
            else:
                self.items.append(
                    self.gc.SPECIAL_SQUARES.pop(self.position))

    def move(self, movement):
        '''This method update the character's position on the grid
        by adding a variable to it. The variable's value depends
        on which key is pressed during gameplay loop'''

        if self.position + movement in self.gc.SQUARE_SET:
            self.position += movement
