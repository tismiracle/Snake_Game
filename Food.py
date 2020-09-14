import random
import pygame
from SETTINGS import *

class Food():

    def generate_food(self):
        self.random_width = random.randrange(0, window_width, bodypart_width)
        self.random_height = random.randrange(0, window_height, bodypart_height)
        self.food = pygame.rect.Rect((self.random_width, self.random_height),(food_width, food_height))
        print(self.food)




#food = Food()
#food.generate_food()