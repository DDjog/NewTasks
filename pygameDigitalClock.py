import pygame

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))

center = (WIDTH//2, HEIGHT//2)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    draw_time()

    pygame.display.update()

    clock.tick(1)

pygame.quit()
def draw_clock():
    pygame.draw.polygon(screen, 'black', (WIDTH, HEIGHT), width =3)

def draw_digits():
