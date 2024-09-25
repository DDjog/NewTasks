import pygame

pygame.init()
screen = pygame.display.set_mode((560, 560))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
    pygame.draw.circle(screen, (255, 0, 0), (150, 150), 33, 3)
    pygame.draw.polygon(screen, (255, 255,0), [(250, 120), (300, 170), (189, 160)])

    pygame.display.flip()

