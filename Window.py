import pygame
from Body import Snake_Body
import SETTINGS
from SETTINGS import *
from Debug import *
from Food import *
from Sounds import *
import random



class Window():
    def __init__(self):
        pygame.init()
        self.counter = 0
        self.index = 0
        self.randomize_tongue = random.randint(0,5)
        self.random = random.randint(0,5)
        self.eat = False

        self.initialize_window()
        #self.sounds = Sounds()
        self.food = Food()
        self.food.generate_food()
        self.debug = Debug(self.screen)
        self.load_tongue()
        self.load_background()
        self.load_snake_sprite()
        self.load_food_sprite()
        self.snake_body = Snake_Body()
        
        self.clock = pygame.time.Clock()
        self.toggle_debug = False
        
        

        self.running = True
        while self.running:            
            self.get_coordinates()
            #self.snake_body.rest_follow()
            
            self.snake_collide()
            
            pygame.display.update()

            #print(self.snake_body.body)
            #if len(self.snake_body.body) > 1:
                #self.snake_body.rest_follow()
            #self.screen.fill((0, 0, 0))
            self.screen.blit(self.background,(0,0))
            self.handle_keys()
            self.continue_moving()
            
            self.display_snake()
            #self.snake_collide()

            self.display_food()
            

            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.clock.tick(60)
            self.count_ticks()
            
            pygame.display.update()
            

    
    def load_background(self):
        self.background = pygame.image.load("Background.png")
        self.background = pygame.transform.scale(self.background, (window_width, window_height))
    
    def load_tongue(self):
        self.tongue_up_animation = []
        self.tongue_down_animation = []
        self.tongue_left_animation = []
        self.tongue_right_animation = []
        for i in range(1,27):
            self.tongue_up_animation.append(pygame.image.load(rf"Tongue\Tongue_up\{i}.png").convert_alpha())
            self.tongue_up_animation[i-1] = pygame.transform.scale(self.tongue_up_animation[i-1],(bodypart_width, bodypart_height))

            self.tongue_down_animation.append(pygame.image.load(rf"Tongue\Tongue_down\{i}.png").convert_alpha())
            self.tongue_down_animation[i-1] = pygame.transform.scale(self.tongue_down_animation[i-1],(bodypart_width, bodypart_height))

            self.tongue_left_animation.append(pygame.image.load(rf"Tongue\Tongue_left\{i}.png").convert_alpha())
            self.tongue_left_animation[i-1] = pygame.transform.scale(self.tongue_left_animation[i-1],(bodypart_width, bodypart_height))

            self.tongue_right_animation.append(pygame.image.load(rf"Tongue\Tongue_right\{i}.png").convert_alpha())
            self.tongue_right_animation[i-1] = pygame.transform.scale(self.tongue_right_animation[i-1],(bodypart_width, bodypart_height))

        print(self.tongue_up_animation)
        print(self.tongue_down_animation)
        print(self.tongue_left_animation)
        print(self.tongue_right_animation)
    


    def animate_tongue(self):
        #self.snake_body.sss()
        if len(self.snake_body.rest_direction) > 1:
            
            if self.snake_body.rest_direction[0] == 3:                
                if self.counter <= len(self.tongue_up_animation)-1:
                    self.screen.blit(self.tongue_up_animation[self.counter], (self.snake_body.body[0].x, self.snake_body.body[0].y - bodypart_height))
            elif self.snake_body.rest_direction[0] == 2:
                if self.counter <= len(self.tongue_down_animation)-1:
                    self.screen.blit(self.tongue_down_animation[self.counter], (self.snake_body.body[0].x, self.snake_body.body[0].y + bodypart_height))

            elif self.snake_body.rest_direction[0] == 1:
                if self.counter <= len(self.tongue_right_animation)-1:
                    self.screen.blit(self.tongue_right_animation[self.counter], (self.snake_body.body[0].x + bodypart_width, self.snake_body.body[0].y))
            elif self.snake_body.rest_direction[0] == 0:
                if self.counter <= len(self.tongue_left_animation)-1:
                    self.screen.blit(self.tongue_left_animation[self.counter], (self.snake_body.body[0].x - bodypart_width, self.snake_body.body[0].y))
        


    def load_snake_sprite(self):
        self.head_up = pygame.image.load("Snake_head\Snake_head.png").convert_alpha()
        self.head_up = pygame.transform.scale(self.head_up,(bodypart_width, bodypart_height))
        self.head_down = pygame.image.load("Snake_head\Snake_head_down.png").convert_alpha()
        self.head_down = pygame.transform.scale(self.head_down,(bodypart_width, bodypart_height))
        self.head_left = pygame.image.load("Snake_head\Snake_head_left.png").convert_alpha()
        self.head_left = pygame.transform.scale(self.head_left,(bodypart_width, bodypart_height))
        self.head_right = pygame.image.load("Snake_head\Snake_head_right.png").convert_alpha()
        self.head_right = pygame.transform.scale(self.head_right,(bodypart_width, bodypart_height))

        self.head_happy_up = pygame.image.load("Snake_head\Snake_happy\Snake_head_happy_up.png").convert_alpha()
        self.head_happy_up = pygame.transform.scale(self.head_happy_up, (bodypart_width, bodypart_height))
        self.head_happy_down = pygame.image.load("Snake_head\Snake_happy\Snake_head_happy_down.png").convert_alpha()
        self.head_happy_down = pygame.transform.scale(self.head_happy_down, (bodypart_width, bodypart_height))
        self.head_happy_left = pygame.image.load("Snake_head\Snake_happy\Snake_head_happy_left.png").convert_alpha()
        self.head_happy_left = pygame.transform.scale(self.head_happy_left, (bodypart_width, bodypart_height))
        self.head_happy_right = pygame.image.load("Snake_head\Snake_happy\Snake_head_happy_right.png").convert_alpha()
        self.head_happy_right = pygame.transform.scale(self.head_happy_right, (bodypart_width, bodypart_height))


        self.body_up = pygame.image.load("Snake_body\Snake_body_up.png").convert_alpha()
        self.body_up = pygame.transform.scale(self.body_up, (bodypart_width, bodypart_height))
        self.body_down = pygame.image.load("Snake_body\Snake_body_down.png").convert_alpha()
        self.body_down = pygame.transform.scale(self.body_down, (bodypart_width, bodypart_height))
        self.body_left = pygame.image.load("Snake_body\Snake_body_left.png").convert_alpha()
        self.body_left = pygame.transform.scale(self.body_left, (bodypart_width, bodypart_height))
        self.body_right = pygame.image.load("Snake_body\Snake_body_right.png").convert_alpha()
        self.body_right = pygame.transform.scale(self.body_right, (bodypart_width, bodypart_height))



    def load_food_sprite(self):
        self.food_image = pygame.image.load("Food\Food.png").convert_alpha()
        self.food_image = pygame.transform.scale(self.food_image, (food_width, food_height))


        


    def count_ticks(self):
        if self.counter > 60:

            self.counter = 0
        else:
            self.counter += 1


    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] or key[pygame.K_UP]:

            print("Go up")
            self.snake_body.set_up()

        if key[pygame.K_s] or key[pygame.K_DOWN]:

            print("Go down")
            self.snake_body.set_down()

        if key[pygame.K_a] or key[pygame.K_LEFT]:

            print("Go left")
            self.snake_body.set_left()
        if key[pygame.K_d] or key[pygame.K_RIGHT]:

            print("Go right")
            self.snake_body.set_right()
        if key[pygame.K_ESCAPE]:
            print('ESCAPE clicked')
            self.running = False

        if key[pygame.K_F12]:
            self.toggle_debug = True
            self.debug.generate_grid()

        if key[pygame.K_F11]:
            self.toggle_debug = False


    def initialize_window(self):
        pygame.display.set_caption("Program")
        self.screen = pygame.display.set_mode((window_width, window_height))


    def display_snake(self):
        self.body = self.snake_body.body
        
        if self.counter == 60 or self.counter == 30:
            print("random")
            self.random = random.randrange(0,5)
        if self.randomize_tongue == self.random:
            #print("SSS")
            for i in range(0,30):
                #print(i)
                self.randomize_tongue == self.random
                self.animate_tongue()
                
            
        #print(self.body)
        if self.toggle_debug:

            for value, bodypart in enumerate(self.body):
                if len(self.snake_body.rest_direction) == 0:
                    self.screen.blit(self.head_up, (bodypart.x, bodypart.y))
                    break
                elif value == 0:
            
                    if self.snake_body.rest_direction[0] == 0:
                        self.screen.blit(self.head_left, (bodypart.x, bodypart.y))
                        
                    if self.snake_body.rest_direction[0] == 1:
                        self.screen.blit(self.head_right, (bodypart.x, bodypart.y))
                        
                    if self.snake_body.rest_direction[0] == 2:
                        self.screen.blit(self.head_down, (bodypart.x, bodypart.y))
                        
                    if self.snake_body.rest_direction[0] == 3:
                        self.screen.blit(self.head_up, (bodypart.x, bodypart.y))
                        
                
                    
                else:
                    
                    if self.snake_body.rest_direction[value] == 0:
                        self.screen.blit(self.body_left, (bodypart.x, bodypart.y))
                        
                    elif self.snake_body.rest_direction[value] == 1:
                        self.screen.blit(self.body_right, (bodypart.x, bodypart.y))
                        
                    elif self.snake_body.rest_direction[value] == 2:
                        self.screen.blit(self.body_down, (bodypart.x, bodypart.y))
                        
                    elif self.snake_body.rest_direction[value] == 3:
                        self.screen.blit(self.body_up, (bodypart.x, bodypart.y))
                        
                

        else:
            for value, bodypart in enumerate(self.body):
                #print(value)
                if len(self.snake_body.rest_direction) == 0:
                    self.screen.blit(self.head_up, (bodypart.x, bodypart.y))
                    
                    break
                elif value == 0:
                    
                    if self.snake_body.rest_direction[0] == 0:
                        if self.eat:
                            
                            self.screen.blit(self.head_happy_left, (bodypart.x, bodypart.y))
                            #self.eat = False
                        else:
                            self.screen.blit(self.head_left, (bodypart.x, bodypart.y))
                        
                    if self.snake_body.rest_direction[0] == 1:
                        if self.eat:
                            
                            self.screen.blit(self.head_happy_right, (bodypart.x, bodypart.y))
                            #self.eat = False
                        else:                        
                            self.screen.blit(self.head_right, (bodypart.x, bodypart.y))
                        
                    if self.snake_body.rest_direction[0] == 2:
                        if self.eat:
                            
                            self.screen.blit(self.head_happy_down, (bodypart.x, bodypart.y))
                            #self.eat = False
                        else:
                            self.screen.blit(self.head_down, (bodypart.x, bodypart.y))
                        
                    if self.snake_body.rest_direction[0] == 3:
                        if self.eat:
                            
                            self.screen.blit(self.head_happy_up, (bodypart.x, bodypart.y))
                            #self.eat = False
                        else:
                            self.screen.blit(self.head_up, (bodypart.x, bodypart.y))
                    
                    #self.eat = False
                
                    
                else:
                    
                    if self.snake_body.rest_direction[value] == 0:                        
                        
                        self.screen.blit(self.body_left, (bodypart.x, bodypart.y))
                        
                        
                        
                    elif self.snake_body.rest_direction[value] == 1:
                        self.screen.blit(self.body_right, (bodypart.x, bodypart.y))
                        
                    elif self.snake_body.rest_direction[value] == 2:
                        self.screen.blit(self.body_down, (bodypart.x, bodypart.y))
                        
                    elif self.snake_body.rest_direction[value] == 3:
                        self.screen.blit(self.body_up, (bodypart.x, bodypart.y))
                    #self.eat = False
                          
                    #elif self.snake_body.rest_direction[0] is None:
                    #    pass
                
                
        


    def display_food(self):
        #food = self.food.food
        food = self.food.food
        #pygame.draw.rect(self.screen, food_colour, food)
        self.screen.blit(self.food_image, (self.food.random_width, self.food.random_height))
        pygame.display.update()

    def continue_moving(self):
        if self.counter == 60 or self.counter == 30:
            self.eat = False
            self.snake_body.rest_follow()
            if self.snake_body.direction == 0:  
                self.snake_body.go_left()

                
                #self.sounds.play_move()
            if self.snake_body.direction == 1:

                self.snake_body.go_right()
 
                
                #self.sounds.play_move()
            if self.snake_body.direction == 2:

                self.snake_body.go_down()

                
                #self.sounds.play_move()
            if self.snake_body.direction == 3:

                self.snake_body.go_up()
  
                
                #self.sounds.play_move()

            #pygame.display.flip()

    def snake_collide(self):
        if self.bodyxy == self.foodxy:
            self.eat = True
            self.food.generate_food()
            self.snake_body.grow()

            


    def get_coordinates(self):
        self.bodyxy = self.snake_body.body[0].center
        self.foodxy = self.food.food.center

        #print(self.bodyxy)
        #print(self.foodxy)

    def reset(self):
        pygame.quit()
        pygame.display.quit()
        Window()





def main():
    app = Window()



if __name__ == "__main__":
    main()



