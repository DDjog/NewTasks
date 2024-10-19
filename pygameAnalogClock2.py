import pygame
import time
import math

pygame.init()
pygame.font.init()

clock_size = 400
screen = pygame.display.set_mode((clock_size, clock_size))

center = (clock_size//2, clock_size//2)
clock_radius = clock_size//2 -9

font = pygame.font.SysFont(None, 40)
clock_color = 'black'

def draw_mark(angle, length, color, width=1, mark_length=10):
    start_x = center[0] + (length-mark_length)*math.cos(math.radians(angle))
    start_y = center[1] - (length - mark_length)*math.sin(math.radians(angle))
    end_x = center[0] + length*math.cos(math.radians(angle))
    end_y = center[1] - length*math.sin(math.radians(angle))
    pygame.draw.line(screen, color, (start_x, start_y), (end_x,end_y), width)

def draw_hand(angle, length, color, width=1):
    end_x = center[0] + length * math.cos(math.radians(angle))
    end_y = center[1] - length * math.sin(math.radians(angle))
    pygame.draw.line(screen, color, center, (end_x, end_y), width)


def draw_digit(angle, length, digit, color):
    digit_x = center[0]+(length - 30)*math.cos(math.radians(angle))
    digit_y = center[1]-(length - 30)*math.sin(math.radians(angle))
    digit_render = font.render(str(digit), True, color)
    digit_rect = digit_render.get_rect(center =(digit_x, digit_y))
    screen.blit(digit_render, digit_rect)

def color_change(new_color):
    global clock_color
    clock_color=new_color

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                color_change('blue')

    screen.fill('white')
    pygame.draw.circle(screen, clock_color, center, clock_radius, 3)

    for i in range(60):
        angle = 90 - i * (360 / 60)
        if i % 5 == 0:
            draw_mark(angle, clock_radius - 2, clock_color, mark_length=15)
            if i % 15 == 0:
                digit = i // 5
                if digit == 0:
                    digit = 12
                draw_digit(angle, clock_radius, digit, clock_color)
        else:
            draw_mark(angle, clock_radius - 2, clock_color, mark_length=7)

    current_time = time.localtime()
    hours = current_time.tm_hour%12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    hour_angle = 90 - (360*(hours + minutes/60)/12)
    minute_angle = 90 - (360*minutes/60)
    second_angle = 90 - (360*seconds/60)

    draw_hand(hour_angle,clock_radius*0.5, clock_color, 6)
    draw_hand(minute_angle, clock_radius * 0.8, clock_color, 4)
    draw_hand(second_angle, clock_radius * 0.9, 'red', 2)

    pygame.display.update()
    pygame.time.Clock().tick(15)

pygame.quit()