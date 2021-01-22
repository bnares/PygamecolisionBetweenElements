import pygame, sys


pygame.init()

clock = pygame.time.Clock()


width = 600
height = 600
screen = pygame.display.set_mode((width, height))

moving_rect = pygame.Rect(350,350,100,100)
x_speed, y_speed = 5,4

other_rect = pygame.Rect(300,200, 200,100)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (255, 255, 255), moving_rect)
    pygame.display.update()
    clock.tick(60)