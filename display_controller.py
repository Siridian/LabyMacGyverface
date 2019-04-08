import pygame


class DisplayController:
    '''handles sprites loading from ressources folder
    also displays them in the window, based on their position on the grid'''

    def __init__(self, game_controller):

        self.SPRITE_WIDTH = 50

        self.TILE_SPRITE = pygame.image.load("ressources/tile.png")
        self.CHARACTER_SPRITE = pygame.image.load("ressources/character.png")
        self.WARDEN_SPRITE = pygame.image.load("ressources/warden.png")
        self.NEEDLE_SPRITE = pygame.image.load("ressources/needle.png")
        self.PIPE_SPRITE = pygame.image.load("ressources/pipe.png")
        self.EHER_SPRITE = pygame.image.load("ressources/ether.png")
        self.WALL_SPRITE = pygame.image.load("ressources/wall.png")
        self.VICTORY_SCREEN = pygame.image.load("ressources/victory.jpg")
        self.DEFEAT_SCREEN = pygame.image.load("ressources/defeat.jpg")

        self.STATE = None

        self.window = None

        self.gc = game_controller

    
    def initialize_display(self):
        pygame.init() #enables sprite initialization during display_controller class declaration
        self.window = pygame.display.set_mode(((self.gc.last_square_position[0] + 1 ) * SPRITE_WIDTH, 
                                               (self.gc.last_square_position[1] + 1 ) * SPRITE_WIDTH))


    def refresh_display(self):
        '''The method is called after each action (i.e when the character moves)
        Each square is refreshed, displaying eventual content atop standard tile'''

        if self.STATE == "Victory":
            window.blit(self.VICTORY_SCREEN, (0, 0))

        elif self.STATE == "Defeat":
            window.blit(self.DEFEAT_SCREEN, (0, 0))

        else:    

            for row in gc.row_array:

                x_pix_pos = index(row) * self.SPRITE_WIDTH

                for square in row :

                    y_pix_pos = index(square) * self.SPRITE_WIDTH

                    window.blit(self.TILE_SPRITE, (x_pix_pos, y_pix_pos))

                    #standard tile is blitted before adding eventual content

                    if square == 1:
                        window.blit(self.WARDEN_SPRITE, (x_pix_pos, y_pix_pos))

                    elif square == 2:
                        window.blit(self.NEEDLE_SPRITE, (x_pix_pos, y_pix_pos))

                    elif square == 3:
                        window.blit(self.PIPE_SPRITE, (x_pix_pos, y_pix_pos))

                    elif square == 4:
                        window.blit(self.ETHER_SPRITE, (x_pix_pos, y_pix_pos))

                    elif square == 5:
                        window.blit(self.WALL_SPRITE, (x_pix_pos, y_pix_pos))

                    elif square == 6:
                        window.blit(self.CHARACTER_SPRITE, (x_pix_pos, y_pix_pos))

        
        pygame.display.flip()