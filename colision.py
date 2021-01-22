import pygame, sys


pygame.init()

clock = pygame.time.Clock()


width = 600
height = 600
screen = pygame.display.set_mode((width, height))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30))
    pygame.display.update()
    clock.tick(60)