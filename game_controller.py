from random import sample
import json

class GameController:
    '''Handles the labyrinth grid creation using dedicated json file
    Created grid is stored as an array of squares used for navigation
    Also contains useful variable to check game state'''


    def __init__(self):
        self.running = True
        self.game_over = False
        self.row_array = []
        self.start_square_position = [0, 0]
        self.last_square_position = [14, 14]


    def initialize_squares(self):
        '''Generates fresh empty grid and add items on it using the method below'''
        self.row_array = []

        for i in range(0, self.last_square_position[0]):

            square_row = []

            for j in range(0, self.last_square_position[1]):

                square_row.append(5)

            self.row_array.append(square_row)

        self.populate_squares()


    def populate_squares(self):
        '''Creates items on squares. Nature of item is defined by an int
        that is stored in the content attribute of the square :
        1 is warden, 2 to 4 are pick-ups, 5 is wall, 6 is character'''
        
        available_squares = []

        for counter, id_key in enumerate(
                json.load(open("ressources/path-layout.json"))):       

            if counter == 0:
                self.row_array[id_key[0]][id_key[1]].content = 6
                self.start_square_position = id_key
            elif counter == 1:
                self.row_array[id_key[0]][id_key[1]] = 1
            else:
                self.row_array[id_key[0]][id_key[1]] = 0
                available_squares.append(id_key)

        for x, position in enumerate(sample(available_squares, 3), 2):
            self.row_array[position[0]][position[1]] = x

        
