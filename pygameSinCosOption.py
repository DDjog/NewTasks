import pygame
import math


width = 630
height = 600
center_y = height // 2
center_x = width // 2
scale = 100

running = True
screen = pygame.display.set_mode((width, height))
mode = 4



def draw_sin(mode):
    for x in range(-center_x, center_x):
        math_x = x / scale
        y = math.sin(math_x)
        screen_y = center_y - int(y* scale)
        pygame.draw.circle(screen, 'red', (center_x + x, screen_y), 2)


def draw_cos(mode):
    for x in range(-center_x, center_x):
        math_x = x / scale
        y = math.cos(math_x)
        screen_y = center_y - int(y * scale)
        pygame.draw.circle(screen, 'green', (center_x + x, screen_y), 2)


print("Menu:\n"
      "1 = Press 1 to draw picture of sinus \n" 
      "2 = Press 2 to draw picture of cosinus \n"
      "3 = Press 3 to draw picture of sinus and cosinus")

pygame.init()


while running:
    screen.fill('white')
    pygame.draw.line(screen, 'black', (0, center_y), (width, center_y), 2)
    pygame.draw.line(screen, 'black', (center_x, 0), (center_x, height), 2)

    if mode == 0:
        draw_sin(mode)
    elif mode == 1:
        draw_cos(mode)
    elif mode == 2:
        draw_sin(mode)
        draw_cos(mode)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = 0
            elif event.key == pygame.K_2:
                mode = 1
            elif event.key == pygame.K_3:
                mode = 2
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    pygame.time.delay(250)


# end of while running

pygame.quit()