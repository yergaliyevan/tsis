import pygame
import sys
from datetime import datetime 
pygame.init()
W,H=500,500
angle1=0
angle2=0
sc=pygame.display.set_mode((W,H))
pygame.display.set_caption("Clock application")
clock = pygame.time.Clock()
FPS = 60
mainclock=pygame.image.load("/Users/mwtl2rua/Downloads/main-clock.png")
mainclock = pygame.transform.scale(mainclock, (W,H))
center=W//2,H//2
min=pygame.image.load("/Users/mwtl2rua/Downloads/right-hand.png").convert_alpha()
minrect=min.get_rect()
sec=pygame.image.load("/Users/mwtl2rua/Downloads/left-hand.png").convert_alpha()
secrect=sec.get_rect()
minrect.center=secrect.center=center
move=True
while move:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            move=False
    now=datetime.now()
    minute=now.minute
    second=now.second

    angle1=-minute*6+84
    rot1=pygame.transform.rotate(min, angle1)
    rect1=rot1.get_rect()
    rect1.center=minrect.center

    angle2=-second*6-282
    rot2=pygame.transform.rotate(sec, angle2)
    rect2=rot2.get_rect()
    rect2.center=secrect.center

    sc.blit(mainclock, (0, 0))
    sc.blit(rot1, rect1)
    sc.blit(rot2, rect2)
    pygame.display.flip()
    clock.tick(FPS)