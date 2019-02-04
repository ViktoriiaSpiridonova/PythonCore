# Написати код анімації квадрата, який переміщається від лівої межі до правої, дотикається до неї, але не зникає за нею. 
# Після цього повертається назад – від правої межі до лівої, дотикається до неї, і знову рухається вправо. 
# Цикли руху квадрата повторюються до завершення програми.

import pygame
pygame.init()
gameDisplay = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Square Game")

PURPLE = (204, 51, 153)
LIGHT_GREEN = (204, 255, 153)

square_x = 0
square_y = 100

square_change_x = 10
# square_change_y=10

run = True

clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    square_x += square_change_x
    # square_y += square_change_y

    # if square_y>450 or square_y<0:
    #     square_change_y *= -1
    if square_x > 400 or square_x < 0:
        square_change_x *= -1

    gameDisplay.fill(LIGHT_GREEN)
    pygame.draw.rect(gameDisplay, PURPLE, [square_x, square_y, 100, 100])
    clock.tick(60)
    pygame.display.update()
pygame.quit()
