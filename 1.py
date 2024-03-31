
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
WIDTH = 400
HEIGHT = 600
SPEED = 5
Score = 0
Coin=0
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("/Users/mwtl2rua/Downloads/PygameTutorial_3_0/AnimatedStreet.png")
 
#Create a white screen 
screen = pygame.display.set_mode((400,600))
screen.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("/Users/mwtl2rua/Downloads/PygameTutorial_3_0/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,WIDTH-40), 0)  
 
      def move(self):
        global Score
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            Score+= 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("/Users/mwtl2rua/Downloads/PygameTutorial_3_0/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,WIDTH-40), 0)  
    def move(self):
        self.rect.move_ip(0,SPEED)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)
             
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1=Coins()
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#start
run=True
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            run=False

        #speed
        if event.type == INC_SPEED:
              SPEED+= 0.5
    
    #
    screen.blit(background, (0, 0))
    scores = font_small.render("Score:"+str(Score), True,BLACK)
    coin_scores = font_small.render("Coins:"+str(Coin), True, GREEN)
    screen.blit(scores, (10, 10))
    screen.blit(coin_scores, (300, 10))
    
    #making cars and coin move
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    #if ДТП occured
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab8\\crash.wav').play()
        screen.fill(RED)
        screen.blit(game_over, (20, 250))
        screen.blit(scores, (165, 330))
        screen.blit(coin_scores, (165, 350))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        run = False
    
    #get coins
    if pygame.sprite.spritecollideany(P1, Coins):
        Coin += 1
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, WIDTH - 40), 0)

    #enemies not getting      
    if pygame.sprite.spritecollideany(C1, enemies):
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, WIDTH - 40), 0)

    pygame.display.update()
    FPS.tick(60)