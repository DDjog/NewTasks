import pygame
import time

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
center = WIDTH // 2, HEIGHT // 2
pygame.init()

main_font = pygame.font.SysFont("Calibri",70)
alarm_sound = pygame.mixer.Sound('mixkit-morning-clock-alarm-1003.wav')

blink = False
alarm = False
_alarm_hour = 0
alarm_minute = 0
alarm_second = 0

_mpos = pygame.mouse.get_pos()
_button_pressed = pygame.mouse.get_pressed()

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

    time_render = main_font.render(current_time, True, text_color)
    time_rect = time_render.get_rect()
    fixed_rect = pygame.Rect(250, 100, 300, 150)
    #fixed_rect.center = center
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


font = pygame.font.SysFont("Calibri", 20)


def draw_alarm_digit(digit, text_color, target_rect):
    digit_render = font.render(digit, True, text_color)
    digit_rect = digit_render.get_rect(center=target_rect.center)
    pygame.draw.rect(screen, 'black', target_rect, 1)
    screen.blit(digit_render, digit_rect)


def draw_alarm_timer():
    # hours rectangles
    hours_rect = pygame.Rect(10, HEIGHT - 200, 250, 150)
    pygame.draw.rect(screen, 'black', hours_rect, 2)

    hours_rects_1st_row = [
        pygame.Rect(55, HEIGHT - 180, 40, 20),
        pygame.Rect(115, HEIGHT - 180, 40, 20),
        pygame.Rect(175, HEIGHT - 180, 40, 20)
        ]
    hours_rects_2nd_row = [
        pygame.Rect(25, HEIGHT - 130, 40, 20),
        pygame.Rect(70, HEIGHT - 130, 40, 20),
        pygame.Rect(115, HEIGHT - 130, 40, 20),
        pygame.Rect(160, HEIGHT - 130, 40, 20),
        pygame.Rect(205, HEIGHT - 130, 40, 20),
        pygame.Rect(25, HEIGHT - 105, 40, 20),
        pygame.Rect(70, HEIGHT - 105, 40, 20),
        pygame.Rect(115, HEIGHT - 105, 40, 20),
        pygame.Rect(160, HEIGHT - 105, 40, 20),
        pygame.Rect(205, HEIGHT - 105, 40, 20)
    ]

    for i, rect in enumerate(hours_rects_1st_row):
        draw_alarm_digit(str(i), 'black', rect)
        if rect.collidepoint(_mpos) and _button_pressed[0]:
            _alarm_hour = i

    for i, rect in enumerate(hours_rects_2nd_row):
        draw_alarm_digit(str(i), 'black', rect)
        if rect.collidepoint(_mpos) and _button_pressed[0]:
            _alarm_hour = i

    # minutes rectangles
    minutes_rect = pygame.Rect(275, HEIGHT - 200, 250, 150)
    pygame.draw.rect(screen, 'black', minutes_rect, 2)

    minutes_rects_1st_row = [
        pygame.Rect(320, HEIGHT - 180, 40, 20),
        pygame.Rect(380, HEIGHT - 180, 40, 20),
        pygame.Rect(440, HEIGHT - 180, 40, 20)
        ]
    minutes_rects_2nd_row = [
        pygame.Rect(290, HEIGHT - 130, 40, 20),
        pygame.Rect(335, HEIGHT - 130, 40, 20),
        pygame.Rect(380, HEIGHT - 130, 40, 20),
        pygame.Rect(425, HEIGHT - 130, 40, 20),
        pygame.Rect(470, HEIGHT - 130, 40, 20),
        pygame.Rect(290, HEIGHT - 105, 40, 20),
        pygame.Rect(335, HEIGHT - 105, 40, 20),
        pygame.Rect(380, HEIGHT - 105, 40, 20),
        pygame.Rect(425, HEIGHT - 105, 40, 20),
        pygame.Rect(470, HEIGHT - 105, 40, 20)
    ]

    for i, rect in enumerate(minutes_rects_1st_row):
        draw_alarm_digit(str(i), 'black', rect)
        if rect.collidepoint(_mpos) and _button_pressed[0]:
            _alarm_hour = i

    for i, rect in enumerate(minutes_rects_2nd_row):
        draw_alarm_digit(str(i), 'black', rect)
        if rect.collidepoint(_mpos) and _button_pressed[0]:
            _alarm_hour = i

 # seconds rectangles
    seconds_rect = pygame.Rect(540, HEIGHT - 200, 250, 150)
    pygame.draw.rect(screen, 'black', seconds_rect, 2)

    seconds_rects_1st_row = [
        pygame.Rect(585, HEIGHT - 180, 40, 20),
        pygame.Rect(645, HEIGHT - 180, 40, 20),
        pygame.Rect(705, HEIGHT - 180, 40, 20)
        ]
    seconds_rects_2nd_row = [
        pygame.Rect(555, HEIGHT - 130, 40, 20),
        pygame.Rect(600, HEIGHT - 130, 40, 20),
        pygame.Rect(645, HEIGHT - 130, 40, 20),
        pygame.Rect(690, HEIGHT - 130, 40, 20),
        pygame.Rect(735, HEIGHT - 130, 40, 20),
        pygame.Rect(555, HEIGHT - 105, 40, 20),
        pygame.Rect(600, HEIGHT - 105, 40, 20),
        pygame.Rect(645, HEIGHT - 105, 40, 20),
        pygame.Rect(690, HEIGHT - 105, 40, 20),
        pygame.Rect(735, HEIGHT - 105, 40, 20)
    ]


    for i, rect in enumerate(seconds_rects_1st_row):
        draw_alarm_digit(str(i), 'black', rect)
        if rect.collidepoint(_mpos) and _button_pressed[0]:
            _alarm_hour = i

    for i, rect in enumerate(seconds_rects_2nd_row):
        draw_alarm_digit(str(i), 'black', rect)
        if rect.collidepoint(_mpos) and _button_pressed[0]:
            _alarm_hour = i

    pygame.draw.rect(screen, 'black', rect, 2)

_delay_to_click = 3000
_delay_to_set_up_alarm = 0

running = True

last_time_update_draw = pygame.time.get_ticks()
last_time_click = pygame.time.get_ticks()

while running:
    screen.fill('white')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                alarm = not alarm
                pygame.mixer.Sound.stop(alarm_sound)


        check_alarm()
        draw_alarm_timer()
        pygame.display.flip()
        #_delay_to_set_up_alarm = 1000  # miliseconds
        print("time to draw")


    _mpos = pygame.mouse.get_pos()
    px = _mpos[0]
    py = _mpos[1]
    _button_pressed = pygame.mouse.get_pressed()


    if _delay_to_click == 0 and px >= 41 and px <= 41 + 10 and py >= 337 and py <= 347 and _button_pressed == True:
        print("you click at pos=", px, py)
        _delay_to_click = 3000

    if (pygame.time.get_ticks() - last_time_click) > _delay_to_click:
        print("You clicked at pos =", _mpos)
        _delay_to_click = 0
        last_time_click = pygame.time.get_ticks()

    screen.fill('white')

pygame.quit()








