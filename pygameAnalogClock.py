import pygame
import time
import math

clock_size = 400
screen = pygame.display.set_mode((clock_size, clock_size))

center = (clock_size//2, clock_size//2)
clock_radius = clock_size//2 -9


def draw_mark(angle, length, color, width=1, mark_length=10):
    start_x = center[0] + (length-mark_length)*math.cos(math.radians(angle))
    start_y = center[1] - (length - mark_length)*math.sin(math.radians(angle))
    end_x = center[0] + length*math.cos(math.radians(angle))
    end_y = center[1] - length*math.sin(math.radians(angle))
    pygame.draw.line(screen, color, (start_x, start_y), (end_x,end_y), width)


def draw_hand(angle, length, color, width=1, hand_length=0):
    end_x = center[0] + length * math.cos(math.radians(angle))
    end_y = center[1] - length * math.sin(math.radians(angle))
    pygame.draw.line(screen, color, center, (end_x, end_y), width)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('white')
    pygame.draw.circle(screen, 'black', center, clock_radius, 3)

    for i in range(60):
        angle = 90 - (i*360/60)
        if i%5  == 0:
            draw_mark(angle, clock_radius -2, 'black', width=3, mark_length=15)
        else:
            draw_mark(angle, clock_radius - 2, 'black', width=1, mark_length=10)

    current_time = time.localtime()
    hours = current_time.tm_hour%12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    hour_angle = 90 - (360*(hours + minutes/60)/12)
    minute_angle = 90 - (360*minutes/60)
    second_angle = 90 - (360*seconds/60)

    draw_hand(hour_angle,clock_radius*0.5, 'black', 6)
    draw_hand(minute_angle, clock_radius * 0.8, 'black', 4)
    draw_hand(second_angle, clock_radius * 0.9, 'red', 2)

    pygame.display.update()
    pygame.time.Clock().tick(15)

pygame.quit()