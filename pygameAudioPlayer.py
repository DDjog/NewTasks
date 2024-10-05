import pygame
from pygame import mixer

pygame.init()
mixer.music.load('XX.mp3')
mixer.music.set_volume(0.5)

screen = pygame.display.set_mode((500, 500))

def playSound():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    mixer.music.play()
                elif event.key == pygame.K_b:
                    running = False

        screen.fill('black')
        pygame.display.flip()

playSound()
pygame.quit()
