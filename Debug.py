import pygame
from SETTINGS import *
#from Window import *

class Debug():
    def __init__(self, screen):
        self.screen = screen
        self.lines_list = []

        #self.generate_grid()
    def generate_grid(self):
        for i in range(0, (window_width // bodypart_width)):
            self.lines_list.append(pygame.draw.line(self.screen, lines_colour, (0, bodypart_width * i), (window_width, bodypart_width * i)))
            self.lines_list.append(pygame.draw.line(self.screen, lines_colour, (bodypart_height * i, 0), (bodypart_height * i, window_height)))
        '''for i in range(0, 30):
            self.lines_list.append(pygame.draw.line(self.screen, lines_colour, (0, bodypart_width * i), (window_width, bodypart_width * i)))
            self.lines_list.append(pygame.draw.line(self.screen, lines_colour, (bodypart_height * i, 0), (bodypart_height * i, window_height)))'''
        #print("drawing lines")
        #pygame.display.update()

    def turn_debug_off(self):
        pygame.display.quit()
        pygame.display.init()





