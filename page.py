import pygame
from Button import Button
from zong import zong
import sys

class MainPage:

    def mainpage(self, win_width=1080, win_height=720):
        pygame.init()
        window = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("王源游戏")
        # pygame.display.flip()



        # 背景
        z = zong(window)

        while z.falg:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    z.bird.birdUp()   # 如果小鸟 则向上
                    z.bird.getbird()
            else:
                z.bird.birdDown()
                z.bird.getbird()

            # 背景移动
            z.loop()


class StarkPage:
    def mainpage(self, win_width=1080, win_height=720):
        pygame.init()
        window = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("王源游戏")

        music_file = 'files\dj.mp3'  # 替换为你的音乐文件路径
        # 加载音乐
        pygame.mixer.music.load(music_file)
        # 播放音乐（-1表示循环播放）
        pygame.mixer.music.play(-1)


        image1 = pygame.image.load('files/litang.png')
        new = pygame.transform.rotozoom(image1, 0, 0.95)
        window.blit(new, (0, 0))

        # 创建按钮对象
        button_t1 = Button(window, "开始游戏", (0, 255, 0))
        button_t2 = Button(window, "退出游戏", (255, 0, 0))
        button_t3 = Button(window, "按键和说明", (0, 0, 255))

        # 创建按钮
        button_t1.button(bx1=480, bw=150, bh=70, by1=400)
        button_t2.button(bx1=480, bw=150, bh=70, matrix_color=(255, 0, 0), by1=500)
        button_t3.button(bx1=480, bw=150, bh=70, matrix_color=(0, 0, 255), by1=600)

        # button_t4.button(bx1=480, bw=150, bh=70, matrix_color=(255, 255, 255), by1=600) #说明书

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mw, mh = event.pos
                    button_t1.downButton(mw, mh)
                    button_t2.downButton(mw, mh)
                    button_t3.downButton(mw, mh)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONUP:
                    mw, mh = event.pos
                    button_t1.newupButton()
                    button_t2.newupButton()
                    button_t3.newupButton()

                    if button_t1.oldButton(mw, mh):  # 进入主页面
                        while True:
                            mainpage_a = MainPage()
                            mainpage_a.mainpage()
                            del mainpage_a

                    button_t2.upButton(mw, mh)  # 弹退出

                    if button_t3.oldButton(mw,mh):
                        mainpage_b = Illustrate()
                        mainpage_b.mainpage()
                        del mainpage_b
                        mw, mh = event.pos
                        button_t1.newupButton()
                        button_t2.newupButton()
                        button_t3.newupButton()

                    pygame.display.update()


class Illustrate:
    def mainpage(self, win_width=1080, win_height=720):
        pygame.init()
        window = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("王源游戏")

        str_a = "操作说明: 左键按下跳跃"
        str_b = "剧情说明: 你将扮演丁真珍珠"
        str_c = "是一名维新派成员"
        str_d = "守旧派王源 妖言惑众"
        str_e = "你合理利用跳跃键 躲避传统香烟"
        str_f = "取得电子烟->瑞克五代"

        button_t1 = Button(window, "a", (0, 255, 0))
        button_t1.manyfont(str_a,str_b,str_c,str_d,str_e,str_f,)

        button_t2 = Button(window, "返回", (255, 0, 0))
        button_t2.button(bx1=480, bw=150, bh=70, matrix_color=(255, 0, 0), by1=500)

        pygame.display.flip()
        flga = True
        while flga:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mw, mh = event.pos
                    button_t2.downButton(mw, mh)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONUP:
                    mw, mh = event.pos
                    if button_t2.oldButton(mw, mh):
                        image1 = pygame.image.load('files/litang.png')
                        new = pygame.transform.rotozoom(image1, 0, 0.95)
                        window.blit(new, (0, 0))
                        flga = False  # 说明书类



