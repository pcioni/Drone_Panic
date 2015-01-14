import pygame

class Lives(object):
     def __init__(self, lives=10):
          self.lives = lives
          self.f = pygame.font.Font("Font/pdark.ttf", 64)
          
     def display(self, screen):
          self.screen = self.f.render('Droid Energy:' + str(self.lives), 1, (0, 0, 0))
          self.rect = self.screen.get_rect()
          self.rect.topleft = (80, 400)          
          screen.blit(self.screen, self.rect)
          
     def update_lives(self, lives):
          self.lives = lives