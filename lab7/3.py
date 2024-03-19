import pygame
pygame.init()
w, h = 500, 500
white = (255, 255, 255)
red = (255, 0, 0)
sc = pygame.display.set_mode((w, h))
pygame.display.set_caption("ball")
x = w // 2
y = h // 2
move= True
while move:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            move = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -=20
            elif event.key == pygame.K_DOWN:
                y +=20
            elif event.key == pygame.K_LEFT:
                x -=20
            elif event.key == pygame.K_RIGHT:
                x +=20
    if x < 25:
        x = 25
    elif x > w - 25:
        x = w - 25
    if y < 25:
        y = 25
    elif y > h - 25:
        y = h - 25
    sc.fill(white)
    pygame.draw.circle(sc, red, (x, y), 25)
    pygame.display.update()