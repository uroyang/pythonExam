# pygame 이하는 함수의 라이브러리 import
import pygame

fps = 30
# 게임엔진의 초기화
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
# 이미지를 불러온다
player = pygame.image.load('resources\images\dude.png')
grass = pygame.image.load('resources\images\grass.png')
castle = pygame.image.load('resources\images\castle.png')

keys = [False, False, False, False]
playpos = [100, 200]
# 계속 화면을 보이게 한다
while True:
    # 화면을 깨끗하게 한다
    screen.fill((0, 0, 0))
    # 모든 요소를 다시 그린다
    for x in range(width // grass.get_width() + 1):
        for y in range(width // grass.get_height() + 1):
            screen.blit(grass, (x * 100, y * 100))

    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))

    screen.blit(player, playpos)
    # 게임을 다시 그린다.
    pygame.display.flip()
    # 게임을 종료한다
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = True
            elif event.key == pygame.K_a:
                keys[1] = True
            elif event.key == pygame.K_s:
                keys[2] = True
            elif event.key == pygame.K_d:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False
        if keys[0]:
            playpos[1] = playpos[1] - 5
        elif keys[2]:
            playpos[1] = playpos[1] + 5
        elif keys[1]:
            playpos[0] = playpos[0] - 5
        elif keys[3]:
            playpos[0] = playpos[0] + 5
