import pygame, sys


pygame.init()

clock = pygame.time.Clock()


width = 600
height = 600
screen = pygame.display.set_mode((width, height))

moving_rect = pygame.Rect(50,50,100,100)
x_speed, y_speed = 5,4

other_rect = pygame.Rect(300,200, 100,100)


def bouncing_rect():
    global  x_speed, y_speed
    pygame.draw.rect(screen, (255, 255, 255), moving_rect)
    pygame.draw.rect(screen, (255, 0, 0), other_rect)

    moving_rect.x += x_speed
    moving_rect.y += y_speed

    #basic checking collision
    collision_tollerance = 10
    if moving_rect.colliderect(other_rect):
        if abs(moving_rect.top - other_rect.bottom) <= collision_tollerance:
            y_speed*=-1

        if abs(moving_rect.bottom - other_rect.top)<= collision_tollerance:
            y_speed*=-1

        if abs(moving_rect.left - other_rect.right) <= collision_tollerance:
            x_speed*=-1

        if abs(moving_rect.right - other_rect.left) <= collision_tollerance:
            x_speed*=-1

    if moving_rect.right >= width or moving_rect.left<=0:
        x_speed*=-1

    if moving_rect.bottom >= height or moving_rect.top<=0:
        y_speed *=-1

    return [moving_rect.x, moving_rect.y, x_speed, y_speed]







while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




    screen.fill((30, 30, 30))
    bouncing_rect()
    pygame.display.update()
    clock.tick(60)