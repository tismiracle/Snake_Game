import pygame




class Sounds():
    def __init__(self):
        self.snake_move = pygame.mixer.Sound(r"Music\Snake_move.wav")
        self.snake_eat = pygame.mixer.Sound(r"Music\Snake_eat.wav")




    def play_move(self):
        pygame.mixer.Sound.play(self.snake_move)


    def play_eat(self):
        pygame.mixer.Sound.play(self.snake_eat)

