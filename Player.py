import pygame

class Player(object):
    """Main 'character.' Update and draw"""
    def __init__(self, x=100, y=100):
        self.surf = pygame.image.load("img/arrow.png").convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect()
        self.rect.topleft = (x, y)
        self.rect.width = 50 #overriding width and height from the get_rect, since this is a full spritesheet
        self.rect.height = 50
        self.keymap = [False, False, False, False] #up, down, left, right. Set in the event processing block of the main game code
        self.speed = 350 #px/sec
        self.dt = 0 #elapsed time since the last frame change
        self.timer = 0 #constantly updating representation of the previous frame's time
        self.direction = 0 #same mapping: up, down, left, right. Used to determine which row of spritesheet to draw
        self.frame = 0 #which column of spritesheet to draw
        self.frame_timer = 0 #accumulated time since the last frame
        self.frame_rate = 5 #frames/sec
        
    def update(self, screen_rect):
        self.dt = pygame.time.get_ticks() - self.timer
        self.timer = pygame.time.get_ticks()
        
        #motion
        if self.keymap[0] == True:
            self.rect.move_ip(0, -self.speed * self.dt/1000.0)
            self.direction = 0
        if self.keymap[1] == True:
            self.rect.move_ip(0, self.speed * self.dt/1000.0)
            self.direction = 1
        if self.keymap[2] == True:
            self.rect.move_ip(-self.speed * self.dt/1000.0, 0)
            self.direction = 2
        if self.keymap[3] == True:
            self.rect.move_ip(self.speed * self.dt/1000.0, 0)
            self.direction = 3
        self.rect.clamp_ip(screen_rect)
        
        #animation
        if self.keymap == [False, False, False, False]:
            self.frame = 0 #our motionless "pose"
        else:
            self.frame_timer += self.dt
            if self.frame_timer >= 1000.0/self.frame_rate:
                self.frame_timer = 0
                self.frame += 1
                if self.frame > 3:
                    self.frame = 0
        
    def draw(self, screen):
        screen.blit(self.surf, self.rect, pygame.Rect(self.frame*50, self.direction*50, 50, 50))
        
    def get_rect(self):
        return self.rect