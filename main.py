import pygame

import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра Тир')
icon = pygame.image.load('image/Тир.jpeg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('image/target.png')
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH-target_width)
target_y = random.randint(0,SCREEN_HEIGHT-target_height)

color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

hits = 0  # Счетчик попаданий
start_time = pygame.time.get_ticks()  # Начальное время


running = True

while running:
    current_time = pygame.time.get_ticks()
    if current_time - start_time > 60000:  # Проверяем, прошло ли 1 минута
        running = False
        print(f'Количество попаданий за минуту: {hits}')
        continue

    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x<mouse_x<target_x+target_width and target_y<mouse_y<target_y+target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # Изменить цвет при попадании
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                hits += 1 # Увеличиваем счетчик попаданий


    screen.blit(target_img,(target_x, target_y))

    pygame.display.update()

pygame.quit()

 

