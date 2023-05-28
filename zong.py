import pygame
import sys
from random import randint
from Button import Button
from Background import Background
from Bird import Bird
class zong:

    def getby(self):
        return randint(-250, 0)

    def __init__(self, window):
        self.window = window

        self.background1 = Background(self.window)
        self.background2 = Background(self.window)
        self.background3 = Background(self.window)
        self.background4 = Background(self.window)
        self.background5 = Background(self.window)
        self.background6 = Background(self.window)
        self.by1 = self.getby()
        self.by2 = self.getby()
        self.by3 = self.getby()
        self.by4 = self.getby()
        self.by5 = self.getby()
        self.by6 = self.getby()
        self.bx1 = 1035
        self.bx2 = 850
        self.bx3 = 680
        self.bx4 = 510
        self.bx5 = 300
        self.bx6 = 1225

        self.score = 0

        self.falg = True

        self.background1.litang()

        # 小鸟
        self.bird = Bird(self.window)
        self.bird.getbird()
        pygame.display.update()

    def loop(self):
        # 背景移动
        self.background1.randomBackground(self.bx1, self.by1)
        self.background2.randomBackground(self.bx2, self.by2)
        self.background3.randomBackground(self.bx3, self.by3)
        self.background4.randomBackground(self.bx4, self.by4)
        self.background5.randomBackground(self.bx5, self.by5)
        self.background6.randomBackground(self.bx6, self.by6)
        pygame.display.update()
        if self.background5.getrect().colliderect(self.bird.getrect()) or self.background5.getrerect().colliderect(self.bird.getrect()):

            button_t1 = Button(self.window, "再来一局", (0, 255, 0))
            button_t2 = Button(self.window, "结束游戏", (255, 0, 0))
            button_t3 = Button(self.window, "得分:"+(str(self.score)), (0, 0, 255))
            button_t1.button(bx1=480, bw=150, bh=70, by1=400)
            button_t2.button(bx1=480, bw=150, bh=70, matrix_color=(255, 0, 0), by1=500)
            button_t3.button(bx1=480, bw=150, bh=70, matrix_color=(255, 255, 0), by1=600)
            pygame.display.update()
            while self.falg:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mw, mh = event.pos
                        button_t1.downButton(mw, mh)
                        button_t2.downButton(mw, mh)
                        pygame.display.update()
                    if event.type == pygame.MOUSEBUTTONUP:
                        mw, mh = event.pos
                        button_t1.newupButton()
                        button_t2.newupButton()

                        if button_t1.oldButton(mw,mh):
                            self.falg = False
                            return self.falg
                        button_t2.upButton(mw, mh)  # 弹退出
        elif self.background1.getrect().colliderect(self.bird.getrect()) or self.background1.getrerect().colliderect(self.bird.getrect()):
            button_t1 = Button(self.window, "再来一局", (0, 255, 0))
            button_t2 = Button(self.window, "结束游戏", (255, 0, 0))
            button_t3 = Button(self.window, "得分:" + (str(self.score)), (0, 0, 255))
            button_t1.button(bx1=480, bw=150, bh=70, by1=400)
            button_t2.button(bx1=480, bw=150, bh=70, matrix_color=(255, 0, 0), by1=500)
            button_t3.button(bx1=480, bw=150, bh=70, matrix_color=(255, 255, 0), by1=600)
            pygame.display.update()
            while self.falg:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mw, mh = event.pos
                        button_t1.downButton(mw, mh)
                        button_t2.downButton(mw, mh)
                        pygame.display.update()
                    if event.type == pygame.MOUSEBUTTONUP:
                        mw, mh = event.pos
                        button_t1.newupButton()
                        button_t2.newupButton()

                        if button_t1.oldButton(mw, mh):
                            self.falg = False
                            return self.falg
                        button_t2.upButton(mw, mh)  # 弹退出
        elif self.background2.getrect().colliderect(self.bird.getrect()) or self.background2.getrerect().colliderect(self.bird.getrect()):
            button_t1 = Button(self.window, "再来一局", (0, 255, 0))
            button_t2 = Button(self.window, "结束游戏", (255, 0, 0))
            button_t3 = Button(self.window, "得分:" + (str(self.score)), (0, 0, 255))
            button_t1.button(bx1=480, bw=150, bh=70, by1=400)
            button_t2.button(bx1=480, bw=150, bh=70, matrix_color=(255, 0, 0), by1=500)
            button_t3.button(bx1=480, bw=150, bh=70, matrix_color=(255, 255, 0), by1=600)
            pygame.display.update()
            while self.falg:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mw, mh = event.pos
                        button_t1.downButton(mw, mh)
                        button_t2.downButton(mw, mh)
                        pygame.display.update()
                    if event.type == pygame.MOUSEBUTTONUP:
                        mw, mh = event.pos
                        button_t1.newupButton()
                        button_t2.newupButton()

                        if button_t1.oldButton(mw, mh):
                            self.falg = False
                            return self.falg
                        button_t2.upButton(mw, mh)  # 弹退出
        elif self.background3.getrect().colliderect(self.bird.getrect()) or self.background3.getrerect().colliderect(self.bird.getrect()):
            button_t1 = Button(self.window, "再来一局", (0, 255, 0))
            button_t2 = Button(self.window, "结束游戏", (255, 0, 0))
            button_t3 = Button(self.window, "得分:" + (str(self.score)), (0, 0, 255))
            button_t1.button(bx1=480, bw=150, bh=70, by1=400)
            button_t2.button(bx1=480, bw=150, bh=70, matrix_color=(255, 0, 0), by1=500)
            button_t3.button(bx1=480, bw=150, bh=70, matrix_color=(255, 255, 0), by1=600)
            pygame.display.update()
            while self.falg:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mw, mh = event.pos
                        button_t1.downButton(mw, mh)
                        button_t2.downButton(mw, mh)
                        pygame.display.update()
                    if event.type == pygame.MOUSEBUTTONUP:
                        mw, mh = event.pos
                        button_t1.newupButton()
                        button_t2.newupButton()

                        if button_t1.oldButton(mw, mh):
                            self.falg = False
                            return self.falg
                        button_t2.upButton(mw, mh)  # 弹退出
        elif self.background4.getrect().colliderect(self.bird.getrect()) or self.background4.getrerect().colliderect(self.bird.getrect()):
            button_t1 = Button(self.window, "再来一局", (0, 255, 0))
            button_t2 = Button(self.window, "结束游戏", (255, 0, 0))
            button_t3 = Button(self.window, "得分:" + (str(self.score)), (0, 0, 255))
            button_t1.button(bx1=480, bw=150, bh=70, by1=400)
            button_t2.button(bx1=480, bw=150, bh=70, matrix_color=(255, 0, 0), by1=500)
            button_t3.button(bx1=480, bw=150, bh=70, matrix_color=(255, 255, 0), by1=600)
            pygame.display.update()
            while self.falg:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mw, mh = event.pos
                        button_t1.downButton(mw, mh)
                        button_t2.downButton(mw, mh)
                        pygame.display.update()
                    if event.type == pygame.MOUSEBUTTONUP:
                        mw, mh = event.pos
                        button_t1.newupButton()
                        button_t2.newupButton()

                        if button_t1.oldButton(mw, mh):
                            self.falg = False
                            return self.falg
                        button_t2.upButton(mw, mh)  # 弹退出
        elif self.background6.getrect().colliderect(self.bird.getrect()) or self.background6.getrerect().colliderect(self.bird.getrect()):
            button_t1 = Button(self.window, "再来一局", (0, 255, 0))
            button_t2 = Button(self.window, "结束游戏", (255, 0, 0))
            button_t3 = Button(self.window, "得分:" + (str(self.score)), (0, 0, 255))
            button_t1.button(bx1=480, bw=150, bh=70, by1=400)
            button_t2.button(bx1=480, bw=150, bh=70, matrix_color=(255, 0, 0), by1=500)
            button_t3.button(bx1=480, bw=150, bh=70, matrix_color=(255, 255, 0), by1=600)
            pygame.display.update()
            while self.falg:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mw, mh = event.pos
                        button_t1.downButton(mw, mh)
                        button_t2.downButton(mw, mh)
                        pygame.display.update()
                    if event.type == pygame.MOUSEBUTTONUP:
                        mw, mh = event.pos
                        button_t1.newupButton()
                        button_t2.newupButton()

                        if button_t1.oldButton(mw, mh):
                            self.falg = False
                            return self.falg
                        button_t2.upButton(mw, mh)  # 弹退出
        self.bx1 -= 5
        self.bx2 -= 5
        self.bx3 -= 5
        self.bx4 -= 5
        self.bx5 -= 5
        self.bx6 -= 5

        self.background1.litang()
        if self.bx1 < -45:
            self.bx1 = 1035
            self.by1 = self.getby()
        elif self.bx2 < -45:
            self.bx2 = 1035
            self.by2 = self.getby()
        elif self.bx3 < -45:
            self.bx3 = 1035
            self.by3 = self.getby()
        elif self.bx4 < -45:
            self.bx4 = 1035
            self.by4 = self.getby()
        elif self.bx5 < -45:
            self.bx5 = 1035
            self.by5 = self.getby()
        elif self.bx6 < -45:
            self.bx6 = 1035
            self.by6 = self.getby()
        if self.background1.getX() == 120:
            self.score += 1
        elif self.background2.getX() == 120:
            self.score += 1
        elif self.background3.getX() == 120:
            self.score += 1
        elif self.background4.getX() == 120:
            self.score += 1
        elif self.background5.getX() == 120:
            self.score += 1
        elif self.background6.getX() == 120:
            self.score += 1
    def getfalg(self):
        return self.falg