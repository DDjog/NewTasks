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
_alarm_hour_first_digit = 0
_alarm_hour_second_digit = 0

_alarm_minute = 0
_alarm_minute_first_digit = 0
_alarm_minute_second_digit = 0


_alarm_second = 0
_alarm_second_first_digit = 0
_alarm_second_second_digit = 0

_mpos = pygame.mouse.get_pos()
_button_pressed = pygame.mouse.get_pressed()

hours_rect = pygame.Rect(10, HEIGHT - 200, 250, 150)

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

minutes_rect = pygame.Rect(275, HEIGHT - 200, 250, 150)

minutes_rects_1st_row = [
        pygame.Rect(276, HEIGHT - 180, 35, 20),
        pygame.Rect(320, HEIGHT - 180, 35, 20),
        pygame.Rect(363, HEIGHT - 180, 35, 20),
        pygame.Rect(406, HEIGHT - 180, 35, 20),
        pygame.Rect(448, HEIGHT - 180, 35, 20),
        pygame.Rect(490, HEIGHT - 180, 35, 20),
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

seconds_rect = pygame.Rect(540, HEIGHT - 200, 250, 150)

seconds_rects_1st_row = [
        pygame.Rect(540, HEIGHT - 180, 35, 20),
        pygame.Rect(583, HEIGHT - 180, 35, 20),
        pygame.Rect(626, HEIGHT - 180, 35, 20),
        pygame.Rect(669, HEIGHT - 180, 35, 20),
        pygame.Rect(712, HEIGHT - 180, 35, 20),
        pygame.Rect(755, HEIGHT - 180, 35, 20),
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
    global blink, alarm, _alarm_t


    current_time = time.strftime("%H:%M:%S")
    # alarm_time = "20:02:30"

    if current_time == _alarm_t:
        if not alarm:
            pygame.mixer.Sound.play(alarm_sound)
            alarm = True
    if alarm:
        blink = not blink
        draw_time(alarm=True, blink=blink)
    else:
        draw_time(alarm=False, blink=blink)


font = pygame.font.SysFont("Calibri", 20)


def draw_alarm_digit(digit, text_color, rect):
    digit_render = font.render(digit, True, text_color)
    digit_rect = digit_render.get_rect(center=rect.center)
    pygame.draw.rect(screen, 'black', rect, 1)
    screen.blit(digit_render, digit_rect)


def set_alarm_time():

    global _alarm_hour
    global _alarm_hour_first_digit
    global _alarm_hour_second_digit

    global _alarm_minute
    global _alarm_minute_first_digit
    global _alarm_minute_second_digit

    global _alarm_second
    global _alarm_second_first_digit
    global _alarm_second_second_digit

    global _alarm_t

    for i, rect in enumerate(hours_rects_1st_row):
        if rect.collidepoint(_mpos) and _button_pressed[0]==1:
            _alarm_hour_first_digit = i
            _alarm_hour_second_digit = 0
            _alarm_hour = _alarm_hour_first_digit*10 + _alarm_hour_second_digit
            print("Set hour alarm to", _alarm_hour)

    for i, rect in enumerate(hours_rects_2nd_row):
        if rect.collidepoint(_mpos) and _button_pressed[0] == 1:
            _alarm_hour_second_digit = i
            _alarm_hour = _alarm_hour_first_digit * 10 + _alarm_hour_second_digit
            print("Set hour alarm to", _alarm_hour)

    for i, rect in enumerate(minutes_rects_1st_row):
        draw_alarm_digit(str(i), 'black', rect)
        if rect.collidepoint(_mpos) and _button_pressed[0] == 1:
            _alarm_minute_first_digit = i
            _alarm_minute_second_digit = 0
            _alarm_minute = _alarm_minute_first_digit * 10 + _alarm_minute_second_digit
            print("Set minute alarm  to", _alarm_minute)

    for i, rect in enumerate(minutes_rects_2nd_row):
            draw_alarm_digit(str(i), 'black', rect)
            if rect.collidepoint(_mpos) and _button_pressed[0] == 1:
                _alarm_minute_second_digit = i
                _alarm_minute = _alarm_minute_first_digit * 10 + _alarm_minute_second_digit
                print("Set minute alarm to", _alarm_minute)

    for i, rect in enumerate(seconds_rects_1st_row):
        draw_alarm_digit(str(i), 'black', rect)
        if rect.collidepoint(_mpos) and _button_pressed[0] == 1:
            _alarm_second_first_digit = i
            _alarm_second_second_digit = 0
            _alarm_second = _alarm_second_first_digit * 10 + _alarm_second_second_digit
            print("Set second alarm to", _alarm_second)

    for i, rect in enumerate(seconds_rects_2nd_row):
        draw_alarm_digit(str(i), 'black', rect)
        if rect.collidepoint(_mpos) and _button_pressed[0] == 1:
            _alarm_second_second_digit = i
            _alarm_second = _alarm_second_first_digit * 10 + _alarm_second_second_digit
            print("Set second alarm to", _alarm_second)

    _alarm_t = f"{_alarm_hour:02}:{_alarm_minute:02}:{_alarm_second:02}"


    print("Alarm time:", _alarm_t)

def draw_alarm_rect():

    pygame.draw.rect(screen, 'black', hours_rect, 2)
    for i, rect in enumerate(hours_rects_1st_row):
        draw_alarm_digit(str(i), 'black', rect)
    for i, rect in enumerate(hours_rects_2nd_row):
        draw_alarm_digit(str(i), 'black', rect)

    pygame.draw.rect(screen, 'black', minutes_rect, 2)
    for i, rect in enumerate(minutes_rects_1st_row):
        draw_alarm_digit(str(i), 'black', rect)
    for i, rect in enumerate(minutes_rects_2nd_row):
        draw_alarm_digit(str(i), 'black', rect)

    pygame.draw.rect(screen, 'black', seconds_rect, 2)
    for i, rect in enumerate(seconds_rects_1st_row):
        draw_alarm_digit(str(i), 'black', rect)
    for i, rect in enumerate(seconds_rects_2nd_row):
        draw_alarm_digit(str(i), 'black', rect)


def draw_set_alarm_time():

    global _alarm

    set_alarm_rect = pygame.Rect(250, 300, 300, 30)
    alarm_text = f"Alarm was set at {_alarm_hour:02}:{_alarm_minute:02}:{_alarm_second:02}"
    alarm_text_render = font.render(alarm_text, True, 'black')
    alarm_text_rect = alarm_text_render.get_rect(center=(set_alarm_rect.centerx, set_alarm_rect.top + 15))
    screen.blit(alarm_text_render, alarm_text_rect)



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


        set_alarm_time()
        draw_alarm_rect()
        draw_set_alarm_time()
        check_alarm()
        pygame.display.flip()

    _mpos = pygame.mouse.get_pos()
    px = _mpos[0]
    py = _mpos[1]
    _button_pressed = pygame.mouse.get_pressed()

    if _delay_to_click == 0 and px >= 41 and px <= 41 + 10 and py >= 337 and py <= 347 and _button_pressed == True:
        # print("you click at pos=", px, py)
        _delay_to_click = 3000

    if (pygame.time.get_ticks() - last_time_click) > _delay_to_click:
        # print("You clicked at pos =", _mpos)
        _delay_to_click = 0
        last_time_click = pygame.time.get_ticks()



pygame.quit()








