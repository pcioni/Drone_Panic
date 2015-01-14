#import statements
import pygame
import random
from Player import *
from Ball import *
from Score import *
from Lives import *

"""
***************************
GRADE DISTRIBUTION:
TECHNOLOGY: 40%
MECHANICS: 30%
STORY: 10%
ART: 20%

Note:
Game mechanics are sometimes unreliable and obtuse. 
"""

#initialize objects
pygame.init()

screen = pygame.display.set_mode((850, 550))
screen_rect = screen.get_rect()

balls = []
used_letters = [] #dont make balls with the same letter

#Ball variables
difficulty = 1.0
score_multiplier = 1.0
score = 0
lives_counter = 10
scoreboard = Score(score) # initialize the score display
lives = Lives(lives_counter)

title_screen = pygame.image.load("img/title.png").convert()
game_over_screen = pygame.image.load("img/gameover.png").convert()
background = pygame.image.load("img/bg.png").convert()
newlevelbg = pygame.image.load("img/newlevel.png").convert()
storyboard = pygame.image.load("img/story.png").convert()

player = Player(125, 30)
game_over = False
clock = pygame.time.Clock()
new_level = True
init_level = True
titlepass = False #initializes a new game/causes the title screen to display
timer = pygame.time.get_ticks()

color = [((0, 255, 255)), ((0, 0, 255)), ((127, 255, 0)), ((255, 140, 0)), ((255, 20, 147)), ((0, 250, 154)), ((240, 148, 148))] 
#               aqua             blue         chartreuse         orange             pink          spring green         magenta 

screen.blit(title_screen, screen_rect) #display the title screen
pygame.display.flip()


while titlepass == False: 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:  #waits for the player for press enter at the title screen
            if event.key == pygame.K_RETURN:
                titlepass = True

screen.blit(storyboard, screen_rect)
pygame.display.flip()

while init_level == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: #waits for the player for press enter at the title screen 
            
            if event.key == pygame.K_1:
                score_multiplier = 1
                difficulty = 1
                init_level = False
            if event.key == pygame.K_2:
                score_multiplier = 1.5
                difficulty = 1.5
                init_level = False    
            if event.key == pygame.K_3:
                score_multiplier = 2
                difficulty = 2.25
                init_level = False             
            if event.key == pygame.K_4:
                score_multiplier = 10
                difficulty = 3.15
                init_level = False

if difficulty == 1:
    py_keys = [pygame.K_q, pygame.K_e, pygame.K_r, pygame.K_f, pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v]
    letters = 'QERFZXCV' #doesnt include ASDW, as those are movement controls.
    letters = [x for x in letters] 
    hotkeys = dict(zip(letters, py_keys))  #generate a dictionary of hotkeys for each letter
    max_balls = int(20 * difficulty)
    max_dx_dy = int(1 * difficulty)
    min_radius = int(10 * difficulty)
    max_radius = int(15 * difficulty)
    maxx = 850
    maxy = 550 
    
elif difficulty == 1.5:
    py_keys = [pygame.K_q, pygame.K_e, pygame.K_r, pygame.K_f, pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v, pygame.K_t, pygame.K_g, pygame.K_b]
    letters = 'QERFZXCVTGB' #first five columns of the keyboard
    letters = [x for x in letters]     
    hotkeys = dict(zip(letters, py_keys))  
    max_balls = int(20 * difficulty)
    max_dx_dy = int(1 * difficulty)
    min_radius = int(6 * difficulty)
    max_radius = int(20 * difficulty)
    maxx = 850
    maxy = 550 
    
elif difficulty == 2.25:
    py_keys = [pygame.K_q, pygame.K_e, pygame.K_r, pygame.K_f, pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v, pygame.K_t, pygame.K_g, pygame.K_b, pygame.K_y, pygame.K_h, pygame.K_n]
    letters = 'QERFZXCVTGBYHN' #first 6 columns of the keyboard
    letters = [x for x in letters] 
    hotkeys = dict(zip(letters, py_keys))   
    max_balls = int(10 * difficulty)
    max_dx_dy = int(1 * difficulty)
    min_radius = int(3 * difficulty)
    max_radius = int(5 * difficulty)
    maxx = 850
    maxy = 550 
    
elif difficulty == 3.15:
    py_keys = [pygame.K_q, pygame.K_e, pygame.K_r, pygame.K_f, pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v, pygame.K_t, pygame.K_g, pygame.K_b, pygame.K_y, pygame.K_h, pygame.K_n, pygame.K_u, pygame.K_j, pygame.K_m, pygame.K_i, pygame.K_k, pygame.K_o, pygame.K_l, pygame.K_p]
    letters = 'QERFZXCVTGBYHNUJMIKLOP'  #A-Z minus asdw
    letters = [x for x in letters] 
    hotkeys = dict(zip(letters, py_keys))    
    max_balls = int(9 * difficulty)
    max_dx_dy = int(1 * difficulty)
    min_radius = int(5 * difficulty)
    max_radius = int(6 * difficulty)
    maxx = 850
    maxy = 550 
    
for b in balls:
    print str(b)

#ACTUALLY RUNNING THE GAME
#main render loop

render_new_balls = True

while new_level == True:
    if render_new_balls == True: #dont render new balls until the user presses enter. Only render on list!
        letters = 'QERFZXCV'
        letters = [x for x in letters]    
        balls = []
        for x in range(0, max_balls):  #generate the list of randomized ball objects
            if len(letters) > 0:
                if x == 0:
                    new_ball = Ball(random.randint(max_radius, (maxx-max_radius)), random.randint(max_radius, (maxy-max_radius)), random.randint(-max_dx_dy, max_dx_dy)+.1, random.randint(-max_dx_dy, max_dx_dy)+.1, random.randint(min_radius, max_radius), random.choice(color), random.choice(letters), True)
                    # ^ +.1 to dx/dy values so they don't come out as zero.
                    
                    balls.append(new_ball)
                    letters.remove(new_ball.get_letter()) #remove letter redundancy
                    b_key = new_ball.get_letter() #store the key needed to win
                    #always make the first ball the "secret identity" for simplicity. Since everything is random, this doesnt matter much. 
                else:
                    new_ball = Ball(random.randint(max_radius, (maxx-max_radius)), random.randint(max_radius, (maxy-max_radius)), random.randint(-max_dx_dy, max_dx_dy)+.1, random.randint(-max_dx_dy, max_dx_dy)+.1, random.randint(min_radius, max_radius), random.choice(color), random.choice(letters), False)
                    
                    balls.append(new_ball)  
                    letters.remove(new_ball.get_letter())
            else:
                new_ball = random.choice(balls)
                balls.append(new_ball)             
        render_new_balls = False
        
    screen.blit(newlevelbg, screen_rect)
    scoreboard.display(screen)
    pygame.display.flip()
    
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    new_level = False 
                    
    while not game_over and lives_counter > 0 and new_level == False:
                                
            
        #tick clock. 
        clock.tick(30)  
        
        #process events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                elif event.key == pygame.K_w:
                    player.keymap[0] = True
                elif event.key == pygame.K_s:
                    player.keymap[1] = True
                if event.key == pygame.K_a:
                    player.keymap[2] = True
                elif event.key == pygame.K_d:
                    player.keymap[3] = True
                if event.key == hotkeys[b_key]: #initialize the keypress for the "Secret identity" ball
                    render_new_balls = True 
                    new_level = True
                    difficulty += .05 # up the difficulty
                    score += ( ( 1 + lives_counter ) * score_multiplier) #add to the player's score
                    scoreboard.update_score(score)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.keymap[0] = False
                elif event.key == pygame.K_s:
                    player.keymap[1] = False
                if event.key == pygame.K_a:
                    player.keymap[2] = False
                elif event.key == pygame.K_d:
                    player.keymap[3] = False
                    
        #update world
        player.update(screen_rect)
        
        #draw world
        screen.blit(background, screen_rect)
        
        lives.display(screen)
        
        for b in balls:
            f = pygame.font.Font(None, int(b.get_radius()+17))
            b_box = b.bounding_box()
            b_box[0] += 7 #help adjust the numbers to a nice position
            b_box[1] += 5
            b_box = (b_box[0], b_box[1], b_box[2], b_box[3])
            font = f.render(b.get_letter(), 1, (0,0,0)) #creates a black font surface text for the ball's letter
            
            pygame.draw.circle(screen, (int(b.get_color()[0]), int(b.get_color()[1]),int(b.get_color()[2])), (int(b.get_position()[0]), int(b.get_position()[1])), int(b.get_radius()))
            
            screen.blit(font, b_box) #prints the letter after the circle
            b.move()
                
            b.check_and_reverse(maxx, maxy)
                
            if b.get_flag() != True:
                for ball in balls:
                    if ball.get_flag() != True:
                        if b != ball:
                            if b.check_collision(ball):
                                b.collide(ball)
            if b.get_rect().colliderect(player.get_rect()):
                if timer + 1500 <= pygame.time.get_ticks(): #invincibiity frames
                    lives_counter -= 1
                    lives.update_lives(lives_counter)
                    timer = pygame.time.get_ticks()

        #draw the player
        player.draw(screen)
        
        #flip video buffers
        pygame.display.flip()

screen.blit(game_over_screen, screen_rect) # displays the game over screen
scoreboard.display(screen)
pygame.display.flip()                      

print "Remote droid has lost connection."