import pygame
import math


width = 630
height = 600
center_y = height // 2
scale = 100

running = True

pygame.init()
screen = pygame.display.set_mode((width, height))

screen.fill('white')

pygame.draw.line(screen, 'black', (0, center_y), (width, center_y), 2)
pygame.draw.line(screen, 'black', (1, 0), (1, height), 2)

for x in range(1, width):
    math_x = x / scale
    y = math.sin(math_x)
    screen_y = center_y - int(y * scale)
    pygame.draw.circle(screen, 'red', (x, screen_y), 2)

for x in range(1, width):
    math_x = (x - 1) / scale
    y = math.cos(math_x)
    screen_y = center_y - int(y * scale)
    pygame.draw.circle(screen, 'green', (x, screen_y), 2)

pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(250)


# end of while running

pygame.quit()

