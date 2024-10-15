import pygame

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))

center = (WIDTH//2, HEIGHT//2)

clock = pygame.time.Clock()

segment_position = {
0: [(5,2), (7,0), (33,0), (35,2), (33,4), (7,4)],
1: [(2,5), (4,7), (4,33), (2,35), (0,33), (0,7)],
2: [(38,5), (36,7), (36,33), (38,35), (40,33), (40,7)],
3: [(5,38), (7,36), (33,36), (35,38), (33,40), (7,40)],
4: [(2,41), (4,43), (4,69), (2,71), (0,69), (0,43)],
5: [(38,41), (36,43), (36,69), (38,71), (40,69), (40,43)],
6: [(5,74), (7,72), (33,72), (35,74), (33, 76), (7,76)]
}

segment_bool = {
0:[True, True, True, False, True, True, True],
1:[False, False, True, False, False, True, False],
2:[True, False, True, True, True, False, True],
3:[True, False, True, True, False, True, True],
4:[False, True, False, True, False, True, False],
5:[True, True, False, True, False, True, True],
6:[True, True, False, False, True, True, True],
7:[True, False, True, False, False, True, False],
8:[True, True, True, True, True, True, True],
9:[True, True, True, True, False, True, True]
}
def draw_digit(screen, position, segment_bool):
    x_offset, y_offset = position
    for i, segment_is_on in enumerate(segment_bool):
        if segment_is_on:
           adjusted_segment_positions = [(x + x_offset, y + y_offset)] for x,y in segment_position[i])
            pygame.draw.polygon(screen, Segment_color, adjusted_segment_positions)

def draw_color(screen, position, color):
    x_offset, y_offset = position
    pygame.draw.circle(screen, color, (x_offset, y_offset + 25), 3)
    pygame.draw.circle(screen, color, (x_offset, y_offset + 50)), 3

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
