import pygame
import math
WIDTH = 700
HEIGHT = 700
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def rotate_point(point, angle, center):
    x, y = point
    cx, cy = center

    dx = x-cx
    dy = y-cy

    new_x = dx*math.cos(angle) - dy*math.sin(angle)
    new_y = dx*math.sin(angle) + dy*math.cos(angle)

    return new_x + cx, new_y + cy

def rotate_rectangle(angle):
    angle_rad = math.radians(angle)
    rect_points = [(350, 50), (350, 350), (250, 350), (250, 50)]
    center = (300, 200)
    rotated_points = [rotate_point(point, angle_rad, center) for point in rect_points]
    pygame.draw.polygon(screen, 'red', rotated_points, width=3)

def rotate_square(angle):
    angle_rad = math.radians(angle)
    squ_points = [(150, 50), (250, 50), (250, 150), (150, 150)]
    center = (200, 100)
    rotated_points = [rotate_point(point, angle_rad, center) for point in squ_points]
    pygame.draw.polygon(screen, 'green', rotated_points, width=3)

def rotate_triangle(angle):
    angle_rad = math.radians(angle)
    tri_points = [(250, 120), (300, 170), (189, 160)]
    center_x = (250+300+189)/3
    center_y = (120+170+160)/3
    center = (center_x, center_y)
    rotated_points = [rotate_point(point, angle_rad, center) for point in tri_points]
    pygame.draw.polygon(screen, 'blue', rotated_points, width=3)

running = True
angle = 0
mode = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = 1
            elif event.key == pygame.K_2:
                mode = 2
            elif event.key == pygame.K_3:
                mode = 3

    screen.fill('black')
    angle+=1

    if mode == 1:
        rotate_rectangle(angle)
    elif mode == 2:
        rotate_square(angle)
    elif mode == 3:
        rotate_triangle(angle)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()