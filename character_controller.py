class Macgyver:
    '''The MacGyver class represents the player-controlled character
    It handles movement, item pick-up, item storage, and game over
    '''

    def __init__(self, start_pos, game_controller, display_controller):
        '''Constructor spawns the character at a given square on the grid'''
        self.position = start_pos
        self.items = []
        self.current_square.content = 6
        self.gc = game_controller
        self.display = display_controller

    @property
    def current_square(self):
        '''Syntactic sugar'''
        return gc.row_array[self.position[0]][self.position[1]]


    ### SQUARE INTERACTION ###

    def touch_square(self):
        '''Triggers various events when the character enters an occupied square
        Items will be added to inventory
        Encounter with the warden results in either victory or defeat'''
        new_square = self.current_square
        if new_square.content == 1:
            self.gc.running = False
            self.gc.game_over = True

            if len(self.items) == 3:
                self.display.STATE = "Victory"

            else:
                self.display.STATE = "Defeat"

        elif new_square.content in (2, 3, 4):
            self.add_item(new_square.content)

    def add_item(self, content_id):
        '''Reads entered square's content and add corresponding item to array'''
        switcher = {
            '2': "needle",
            '3': "pipe",
            '4': "ether"
        }
        try:
            self.items.append(switcher(str(content_id)))
        except:
            pass

    def move(self, value, axis):
        new_position = self.position
        new_position[axis] += value
        if new_position[axis] in range(0, (gc.last_square_position[axis] + 1)):
            if gc.SQUARE_ARRAY[new_position[0]][new_position[1]].content != 5 :
                    self.position = new_position