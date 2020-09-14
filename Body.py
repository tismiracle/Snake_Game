import pygame
from SETTINGS import *
from Food import Food
from Sounds import *


class Snake_Body():
    
    def __init__(self):
        self.body = []
        #self.rest_direction = [1]
        self.rest_direction = []
        self.bodypart = pygame.rect.Rect((200,200),(bodypart_width, bodypart_height))
        self.sounds = Sounds()
        
        self.direction = None
        
        self.body.append(self.bodypart)


    def print_body(self):
        print(self.body)

    def check_location(self):
        return self.bodypart.x, self.bodypart.y


    def return_body(self):
        return self.body

    def set_left(self):
        self.direction = 0
        
    def set_right(self):
        self.direction = 1

    def set_down(self):
        self.direction = 2


    def set_up(self):
        self.direction = 3

    

    def go_left(self):
        self.sounds.play_move()
        self.body[0].x -= bodypart_width
        self.rest_direction.insert(0,self.direction)
        print(self.rest_direction)
        if len(self.rest_direction) > len(self.body):
            #self.rest_direction.pop(self.rest_direction[-1])
            self.rest_direction.pop(len(self.rest_direction)-1)
        


    def go_right(self):
        self.sounds.play_move()
        self.body[0].x += bodypart_width
        self.rest_direction.insert(0,self.direction)
        print(self.rest_direction)
        if len(self.rest_direction) > len(self.body):
            #self.rest_direction.pop(self.rest_direction[-1])
            self.rest_direction.pop(len(self.rest_direction)-1)


    def go_down(self):
        self.sounds.play_move()
        self.body[0].y += bodypart_height
        self.rest_direction.insert(0,self.direction)
        print(self.rest_direction)
        if len(self.rest_direction) > len(self.body):
            #self.rest_direction.pop(self.rest_direction[-1])
            self.rest_direction.pop(len(self.rest_direction)-1)

    def go_up(self):
        self.sounds.play_move()
        self.body[0].y -= bodypart_height
        self.rest_direction.insert(0,self.direction)
        print(self.rest_direction)
        if len(self.rest_direction) > len(self.body):
            #self.rest_direction.pop(self.rest_direction[-1])
            self.rest_direction.pop(len(self.rest_direction)-1)

    def grow(self):
        #self.last_position = self.body
        self.sounds.play_eat()
        #self.bodypart = pygame.rect.Rect((self.body[0].x, self.body[0].y), (bodypart_width, bodypart_height))
        self.bodypart = pygame.rect.Rect((bodypart_width - (bodypart_width * 2), bodypart_height - (bodypart_height * 2)), (bodypart_width, bodypart_height))
        #print('POP')
        #self.body.append(self.bodypart)
        self.body.append(self.bodypart)
        self.rest_direction.append(self.direction)

    def rest_follow(self):
        counter = len(self.body)
        #print(counter)
        while counter >= 1:
            if len(self.body) > counter:
                self.body[counter].x = self.body[counter - 1].x
                self.body[counter].y = self.body[counter - 1].y
            counter -= 1




