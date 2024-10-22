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


def draw_time(alarm, blink):
    if alarm and blink:
        current_time = time.strftime("%H %M %S")
    else:
        current_time = time.strftime("%H:%M:%S")
    if alarm:
        screen.fill('red')
        text_color = 'yellow'
    elif not alarm:
        text_color = 'blue'
    else:
        return

    time_render = font.render(current_time, True, text_color)
    time_rect = time_render.get_rect()
    fixed_rect = pygame.Rect(0, 0, 300, 150)
    fixed_rect.center = center
    time_rect.center = fixed_rect.center
    pygame.draw.rect(screen, 'black', fixed_rect, 5)
    screen.blit(time_render, time_rect)


def check_alarm():
    global blink, alarm

    current_time = time.strftime("%H:%M:%S")
    alarm_time = "20:02:30"

    if current_time == alarm_time:
        if not alarm:
            pygame.mixer.Sound.play(alarm_sound)
            alarm = True
    if alarm:
        blink = not blink
        draw_time(alarm=True, blink=blink)
    else:
        draw_time(alarm=False, blink=blink)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                alarm = not alarm
                pygame.mixer.Sound.stop(alarm_sound)


    screen.fill('white')

    check_alarm()

    pygame.display.flip()

    pygame.time.Clock().tick(2)

pygame.quit()






