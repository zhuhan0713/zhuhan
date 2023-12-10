# -*- coding:utf-8 -*-
import pygame, sys, time, random
from pygame.locals import *

redColour = pygame.Color(255, 0, 0)
greenColour = pygame.Color(0, 255, 0)
blueColour = pygame.Color(0, 0, 255)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)
yellowColour =pygame.Color(255, 255, 0)
purpleColour =pygame.Color(255, 0, 255)
brownColour =pygame.Color(150, 75, 75)
DeepPinkColour=pygame.Color(255 ,20 ,147)

#初始化并播放背景音乐
#pygame.mixer.init()  #初始化混音器
#pygame.mixer.music.load('Ken Arai - NEXT TO YOU.mp3')  #加载背景音乐
#pygame.mixer.music.set_volume(0.2)  #设置音量
#pygame.mixer.music.play()   #播放背景音乐


# 定义游戏结束函数。当双方长度相等且头头相撞时，为平局。游戏结束，并显示双方分数。
def gameOver (playSurface,score1,score2):
    gameOverFont = pygame.font.SysFont('arial', 32)
    gameOverSurf = gameOverFont.render('tie   '+'pink:'+str(score1-3)+'   '+'blue:'+str(score2-3), True, greyColour)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 10)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(5)
    main()


# 定义游戏结束函数。当1号玩家撞墙或被2号玩家吃了时，游戏结束，显示1号玩家失败，以及双方分数。
def gameOver1(playSurface,score1,score2):
    gameOverFont = pygame.font.SysFont('arial', 32)
    gameOverSurf = gameOverFont.render('green snake Game Over    '+'pink:'+str(score1-3)+'  '+'blue:'+str(score2-3), True, greyColour)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 10)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(5)
    main()

# 定义游戏结束函数。当2号玩家撞墙或被1号玩家吃了时，游戏结束，显示2号玩家失败，以及双方分数。
def gameOver2(playSurface,score1,score2):
    gameOverFont = pygame.font.SysFont('arial', 32)
    gameOverSurf = gameOverFont.render(' blue snake Game Over    '+'pink'+str(score1-3)+'   '+'blue:'+str(score2-3), True, greyColour)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 10)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(5)
    main()


def main():
    pygame.init()  #pygame初始化
    #显示欢迎界面，有开始游戏和退出游戏两个选项
    title_font = pygame.font.SysFont('arial', 32)
    welcome_words = title_font.render('Welcome to My Snake', True, (0, 0, 0), (255, 255, 255))
    tips_font = pygame.font.SysFont('arial', 24)
    start_game_words = tips_font.render('Click to Start Game', True, (0, 0, 0), (255, 255, 255))
    close_game_words = tips_font.render('Press ESC to Close', True, (0, 0, 0), (255, 255, 255))

    playSurface = pygame.display.set_mode((640, 480), FULLSCREEN, 32)  #全屏显示
    fpsClock = pygame.time.Clock()
    pygame.display.set_caption(u'贪吃蛇')  #欢迎界面，此时未开始游戏
    game_started = False

    #初始化两条蛇的起始位置和长度
    snakePosition1 = [100, 100]
    snakeSegments1 = [[100, 100], [80, 100], [60, 100]]
    snakePosition2 = [200, 200]
    snakeSegments2 = [[200, 200], [180, 200], [160, 200]]
    #初始化树莓的起始位置
    raspberryPosition = [300, 300]
    raspberrySpawned = 1
    #初始化两条蛇的起始方向
    direction1 = 'right'
    direction2 = 'right'
    changeDirection1 = direction1
    changeDirection2 = direction2

    while True:   #游戏循环主体
        for event in pygame.event.get():  #获取事件
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:   #键盘输入
                #方向键控制玩家1
                if event.key == K_RIGHT :
                    changeDirection1 = 'right'
                if event.key == K_LEFT:
                    changeDirection1 = 'left'
                if event.key == K_UP :
                    changeDirection1 = 'up'
                if event.key == K_DOWN :
                    changeDirection1 = 'down'
                #‘W’‘A’‘S’‘D’控制玩家2
                if event.key == ord('d'):
                    changeDirection2 = 'right'
                if event.key == ord('a'):
                    changeDirection2= 'left'
                if event.key == ord('w'):
                    changeDirection2 = 'up'
                if event.key == ord('s'):
                    changeDirection2 = 'down'
                if event.key == K_ESCAPE:  #按动ESC退出游戏
                    pygame.event.post(pygame.event.Event(QUIT))
            elif (not game_started) and event.type == pygame.MOUSEBUTTONDOWN: #在游戏欢迎界面时，根据鼠标位置判断是否开始游戏
                x, y = pygame.mouse.get_pos()
                if 213 <= x <= 422 and 304 <= y <= 342:
                    game_started = True
        playSurface.fill((255, 255, 255))  #游戏画面背景为白色

        if game_started: #开始游戏
            # 判断是否输入了反方向,如果输入相反方向，则方向不改变
            if changeDirection1 == 'right' and direction1 != 'left':
                direction1 = changeDirection1
            if changeDirection1 == 'left' and direction1 != 'right':
                direction1 = changeDirection1
            if changeDirection1 == 'up' and direction1 != 'down':
                direction1 = changeDirection1
            if changeDirection1 == 'down' and direction1 != 'up':
                direction1 = changeDirection1
            if changeDirection2 == 'right' and direction2 != 'left':
                direction2 = changeDirection2
            if changeDirection2 == 'left' and direction2 != 'right':
                direction2 = changeDirection2
            if changeDirection2 == 'up' and direction2 != 'down':
                direction2 = changeDirection2
            if changeDirection2 == 'down' and direction2 != 'up':
                direction2 = changeDirection2
            # 根据方向移动蛇头的坐标
            if direction1 == 'right':
                snakePosition1[0] += 20
            if direction1 == 'left':
                snakePosition1[0] -= 20
            if direction1 == 'up':
                snakePosition1[1] -= 20
            if direction1 == 'down':
                snakePosition1[1] += 20

            if direction2 == 'right':
                snakePosition2[0] += 20
            if direction2 == 'left':
                snakePosition2[0] -= 20
            if direction2 == 'up':
                snakePosition2[1] -= 20
            if direction2 == 'down':
                snakePosition2[1] += 20
            # 增加蛇的长度
            snakeSegments1.insert(0, list(snakePosition1))
            snakeSegments2.insert(0, list(snakePosition2))
            # 判断是否吃掉了树莓
            if snakePosition1[0] == raspberryPosition[0] and snakePosition1[1] == raspberryPosition[1]:
                raspberrySpawned = 0
            else:
                snakeSegments1.pop()
            if snakePosition2[0] == raspberryPosition[0] and snakePosition2[1] == raspberryPosition[1]:
                raspberrySpawned = 0
            else:
                snakeSegments2.pop()
            # 如果吃掉树莓，则重新生成树莓
            if raspberrySpawned == 0:
                x = random.randrange(1, 32)
                y = random.randrange(1, 24)
                raspberryPosition = [int(x * 20), int(y * 20)]  #先随机在任意位置生成一个树莓
                while raspberryPosition in snakePosition1 or raspberryPosition in snakePosition2:  #判断树莓是否声称在蛇的身体上，如果是，则重新生成树莓
                    x = random.randrange(1, 32)
                    y = random.randrange(1, 24)
                    raspberryPosition = [int(x * 20), int(y * 20)]
                raspberrySpawned = 1



            # 刷新pygame显示层，显示两条蛇以及树莓
            playSurface.fill(whiteColour)
            for position in snakeSegments1:
                pygame.draw.rect(playSurface, DeepPinkColour, Rect(position[0], position[1], 20, 20))
            for position in snakeSegments2:
                pygame.draw.rect(playSurface, blueColour, Rect(position[0], position[1], 20, 20))
                colour = random.choice([yellowColour, purpleColour, brownColour, blackColour])
                pygame.draw.rect(playSurface, colour, Rect(raspberryPosition[0], raspberryPosition[1], 20, 20))
            pygame.display.flip()


            # 蛇的位置超出边框就算死亡，或者和另一条蛇相撞。
            score1 = len(snakeSegments1)   #分数
            score2 = len(snakeSegments2)
            if snakePosition1[0] > 620 or snakePosition1[0] < 0:
                 gameOver1(playSurface, score1, score2)
            if snakePosition1[1] > 460 or snakePosition1[1] < 0:
                 gameOver1(playSurface, score1, score2)
            for snakeBody1 in snakeSegments1[1:]:  # 玩家二撞上了玩家一，玩家二失败
                if snakePosition2[0] == snakeBody1[0] and snakePosition2[1] == snakeBody1[1]:
                    gameOver2(playSurface, score1, score2)
            if snakePosition2[0] > 620 or snakePosition2[0] < 0:
                gameOver2(playSurface, score1, score2)
            if snakePosition2[1] > 460 or snakePosition2[1] < 0:
                gameOver2(playSurface, score1, score2)
            for snakeBody2 in snakeSegments2[1:]:  # 玩家一撞上了玩家二，玩家一失败
                if snakePosition1[0] == snakeBody2[0] and snakePosition1[1] == snakeBody2[1]:
                    gameOver1(playSurface, score1, score2)
            if snakePosition1[0] == snakePosition2[0] and snakePosition1[1] == snakePosition2[1]:   # 头碰头，谁长谁赢，否则平局。
                if len(snakeSegments1) > len(snakeSegments2):
                    gameOver2(playSurface, score1, score2)
                elif len(snakeSegments1) < len(snakeSegments2):
                    gameOver1(playSurface, score1, score2)
                else:
                    gameOver(playSurface, score1, score2)

        else:  # 游戏没有开始，显示欢迎界面
            playSurface.blit(welcome_words, (188, 100))
            playSurface.blit(start_game_words, (236, 310))
            playSurface.blit(close_game_words, (233, 350))
        pygame.display.update()
        fpsClock.tick(5)


if __name__ == "__main__":
    main()