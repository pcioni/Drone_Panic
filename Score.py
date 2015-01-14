import pygame

class Score(object):
     def __init__(self, score=0):
          self.score = score
          self.f = pygame.font.Font("Font/TechnoHideo.ttf", 32)
          #surf -- front .render
          #rect -- actual rect of the store
          #rect -- where to place the rect
          
     def display(self, screen):
          self.screen = self.f.render("Score:" + str(self.score), 1, (255, 255, 255))
          self.rect = self.screen.get_rect()
          self.rect.topleft = (350, 400)          
          screen.blit(self.screen, self.rect)
          
     def update_score(self, score):
          self.score += score