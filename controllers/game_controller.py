#! /usr/bin/env python3
# coding: utf-8


'''The game controller module is essential to the game's logic
It is the starting point of the whole project'''


import json
import random


class GameController:
    '''Handles the labyrinth grid creation using dedicated json file
    Created grid is stored as an array of squares used for navigation
    Also contains useful variable to check game state'''
    
    GAME_STATE = "Running"
    START_SQUARE_ID = 0
    SQUARE_SET = []
    ITEM_LIST = ["pipe", "needle", "ether"]
    SPECIAL_SQUARES = {}

    @classmethod
    def initialize_squares(cls):
        '''Reads the path layout from the json and add items on unoccupied squares'''
        cls.SQUARE_SET = json.load(open("ressources/path-layout.json"))
        cls.START_SQUARE_ID = cls.SQUARE_SET[0]

        for item, position in zip(cls.ITEM_LIST,
                                  random.sample(cls.SQUARE_SET[2:],
                                  len(cls.ITEM_LIST))):
            cls.SPECIAL_SQUARES.update({position: item})

        cls.SPECIAL_SQUARES.update({cls.SQUARE_SET[1]: "warden"})
