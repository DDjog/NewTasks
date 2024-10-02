import pygame
WIDTH = 500
HEIGHT = 500
FSP = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def rotate_rectangle(angle):
    img0 = pygame.Surface((250, 50))
    img0.fill('green')
    rotated_img = pygame.transform.rotate(img0, angle)
    rect = rotated_img.get_rect(center=(WIDTH//2, HEIGHT//2))
    return rect


def rotate_square(angle):
    img0 = pygame.Surface((100, 100))
    pygame.draw.rect(img0, 'red', (0, 0, 100, 100))
    rotated_img = pygame.transform.rotate(img0, angle)
    squa = rotated_img.get_rect(center =(WIDTH//2, HEIGHT//2))



def rotate_triangle(angle):
    img0 = pygame.Surface((250, 50))
    pygame.draw.polygon(img0, ('yellow'), [(125, 25), (175, 75), (75, 75)])
    rotated_img = pygame.transform.rotate(img0, angle)
    trian = rotated_img.get_rect(center=(WIDTH//2, HEIGHT//2))



print("Menu:\n"
      "1 = Press 1 to see rotation of rectangle \n" 
      "2 = Press 2 to see rotation of square \n"
      "3 = Press 3 to see rotation of triangle")

angle = 0
mode = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = 1
            elif event.key ==pygame.K_2:
                mode =2
            elif event.key == pygame.K_3:
                mode = 3


    angle -= 1
    screen.fill('black')

    import pygame

    WIDTH = 500
    HEIGHT = 500
    FSP = 30

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()


    def rotate_rectangle(angle):
        img0 = pygame.Surface((250, 50), pygame.SRCALPHA)
        img0.fill('green')
        rotated_img = pygame.transform.rotate(img0, angle)
        rect = rotated_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        return rotated_img, rect


    def rotate_square(angle):
        img0 = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.rect(img0, 'red', (0, 0, 100, 100))
        rotated_img = pygame.transform.rotate(img0, angle)
        squa = rotated_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        return rotated_img, squa

    def rotate_triangle(angle):
        img0 = pygame.Surface((200, 200), pygame.SRCALPHA)
        pygame.draw.polygon(img0, ('yellow'), [(125, 25), (175, 75), (75, 75)])
        rotated_img = pygame.transform.rotate(img0, angle)
        trian = rotated_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        return rotated_img, trian

    print("Menu:\n"
          "1 = Press 1 to see rotation of rectangle \n"
          "2 = Press 2 to see rotation of square \n"
          "3 = Press 3 to see rotation of triangle")

    angle = 0
    mode = None

    running = True
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

        angle -= 1
        screen.fill('black')

        if mode == 1:
            img, rect = rotate_rectangle(angle)
            screen.blit(img, rect)
        elif mode == 2:
            img, squa = rotate_square(angle)
            screen.blit(img, squa)
        elif mode == 3:
            img, trian = rotate_triangle(angle)
            screen.blit(img, trian)

        pygame.display.flip()
        clock.tick(FSP)

    pygame.quit()

    if mode == 1:
        rect1 = rotate_rectangle(angle)
        rect1.center = rect.center

        screen.blit(img, rect1)
    elif mode == 2:
        img, squa = rotate_square(angle)
        screen.blit(img, squa)
    elif mode == 3:
        img, trian = rotate_triangle(angle)
        screen.blit(img, trian)

    pygame.display.flip()
    clock.tick(FSP)


pygame.quit()

