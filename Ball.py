import random
import math
import pygame

class Ball(object):
    
    def __init__(self, xpos, ypos, dx, dy, radius, color, letter, pass_flag):
        self.x = float(xpos)
        self.y = float(ypos)
        self.dx = float(dx)
        self.dy = float(dy)
        self.r = float(radius)
        self.c = color
        self.l = str(letter)
        self.flag = pass_flag

    def __str__(self):
        x = self.x
        y = self.y
        r = self.r
        dx = self.dx
        dy = self.dy
        c = self.c
        l = self.l
        flag = str(self.flag)
        s = "position (%.1f,%.1f), radius %.1f, motion (%.1f,%.1f), color %s, letter %s, flag = %s" % (x, y, r, dx, dy, c, l, flag)
        return s    
    
    def get_position(self):
        return (self.x, self.y)
    
    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
    
    def get_color(self):
        return self.c
    
    def some_inside(self, maxx=850, maxy=550):
        if 0 < self.x + self.r and self.x - self.r < maxx:
            if 0 < self.y + self.r and self.y - self.r < maxy: 
                return True
            else:
                return False
        return False
            
    def get_letter(self):
        return self.l
    
    def get_flag(self):
        return self.flag
    
    def get_radius(self):
        return self.r
    
    def check_collision(self, other):
        # distance = sqrrt((x2 - x1)^2 + (y2 - y1)^2)
        if math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2) <= self.r + other.r:
            return True
        else:
            return False
    
    def check_and_reverse(self, maxx=850, maxy=550):
        if self.x - self.r <= 0  or self.x + self.r >= maxx:
            self.dx = self.dx * (-1)
        if self.y - self.r <= 0 or self.y + self.r >= maxy:
            self.dy = self.dy * (-1)    
        
    def collide(self, other):
        if self.x - self.r >= other.x + other.r: #collide from the right
            self.dx = self.dx * (-1)
            other.dx = other.dx * (-1)
        elif self.x + self.r <= other.x + other.r: #collide from the left
            self.dx = self.dx * (-1)
            other.dx = other.dx * (-1)
        elif self.y - self.r <= other.y + other.r: #collide from the bottom
            self.dy = self.dy * (-1)
            other.dy = other.dy * (-1)          
        elif self.y + self.r >= other.y - other.r: #collide from the top
            self.dy = self.dy * (-1)
            other.dy = other.dy * (-1)  
            
    def bounding_box(self):
        # (top_left_x, top_left_y, bottom_right_x, bottom_right_y)
        x = self.x - self.r
        y = self.y - self.r
        x1 = self.x + self.r
        y1 = self.y + self.r
        return [x, y , x1, y1] #self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r) 
    
    def get_rect(self):
        return pygame.Rect((self.x - self.r), (self.y + self.r), (2 * self.r), (2 * self.r))
    