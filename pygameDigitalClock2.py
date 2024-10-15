import pygame
import time

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
center = WIDTH // 2, HEIGHT // 2
pygame.init()

font = pygame.font.SysFont(None,80)
alarm_sound = pygame.mixer.Sound('mixkit-morning-clock-alarm-1003.wav')

blink = False
alarm = False


def draw_time(alarm):
    current_time = time.strftime("%H:%M:%S")

    if alarm:
        screen.fill('red')
        text_color = 'yellow'
    elif not alarm:
        text_color = 'blue'
    else:
        return

    time_render = font.render(current_time, True, text_color)
    time_rect = time_render.get_rect(center=center)
    pygame.draw.rect(screen, 'black', time_rect.inflate(40,40), 5)
    screen.blit(time_render, time_rect)


def check_alarm():
    global blink, alarm

    current_time = time.strftime("%H:%M:%S")
    alarm_time = "19:35:50"

    if current_time == alarm_time:
        if not alarm:
            pygame.mixer.Sound.play(alarm_sound)
            alarm = True
    if alarm:
        blink = not blink
        if blink:
            draw_time(alarm=blink)
    else:
        draw_time(alarm=False)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('white')

    check_alarm()

    pygame.display.flip()

    pygame.time.Clock().tick(2)

pygame.quit()






