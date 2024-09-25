import pygame

pygame.init()
screen = pygame.display.set_mode((560, 560))
running = True

colors = {
    pygame.K_1: (255, 0, 0),    # Czerwony
    pygame.K_2: (0, 255, 0),    # Zielony
    pygame.K_3: (0, 0, 255),    # Niebieski
    pygame.K_4: (255, 255, 0),  # Żółty
    pygame.K_5: (255, 0, 255),  # Fioletowy
    pygame.K_6: (0, 255, 255),  # Błękitny
    pygame.K_7: (128, 0, 128),  # Purpurowy
    pygame.K_8: (255, 165, 0),  # Pomarańczowy
    pygame.K_9: (128, 128, 128),# Szary
    pygame.K_0: (0, 0, 0)       # Czarny
}


current_color = (0, 255, 0)  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                running = False
            elif event.key in colors:
                current_color = colors[event.key]

    screen.fill(current_color)
    pygame.display.flip()

pygame.quit()