import pygame
pygame.init()

W = 1000
H = 800

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Back To The Past")

FPS = pygame.time.Clock()
x,y = W//2, H//2
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed
    elif keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed


    sc.fill((0, 0, 0))
    pygame.draw.circle(sc, (255, 0, 0), (x, y), 25)
    pygame.display.update()

    FPS.tick(60)