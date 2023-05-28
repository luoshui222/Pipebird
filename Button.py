import pygame
import sys

class Button:
    def __init__(self, window, st, color):
        self.window = window
        self.st = st
        font = pygame.font.Font('files/simsun.ttc', 30)
        self.color = color
        self.font = font
        self.bx1 = None
        self.by1 = None
        self.bh = None
        self.bw = None

    def button(self, bx1=30, by1=100, bw=100, bh=50, matrix_color=(0, 255, 0), color=(0, 0, 0)):
        pygame.draw.rect(self.window, matrix_color, (bx1, by1, bw, bh))
        text1 = self.font.render(self.st, True, color)
        tw1, th1 = text1.get_size()
        tx1 = bx1 + bw / 2 - tw1 / 2
        ty1 = by1 + bh / 2 - th1 / 2
        self.window.blit(text1, (tx1, ty1))
        self.bx1 = bx1
        self.by1 = by1
        self.bw = bw
        self.bh = bh

    def downButton(self, mx, my):
        if self.bx1 <= mx <= self.bx1 + self.bw and self.by1 <= my <= self.by1 + self.bh:
            self.button(bx1=self.bx1, by1=self.by1, bw=self.bw, bh=self.bh, matrix_color=(192, 192, 192))

    def upButton(self, mx, my):
        if self.bx1 <= mx <= self.bx1 + self.bw and self.by1 <= my <= self.by1 + self.bh:
            sys.exit()

    def newupButton(self):
        self.button(bx1=self.bx1, by1=self.by1, bw=self.bw, bh=self.bh, matrix_color=self.color)

    def oldButton(self, mx, my):
        if self.bx1 <= mx <= self.bx1 + self.bw and self.by1 <= my <= self.by1 + self.bh:
            return True
        else:
            return False

    def manyfont(self, a, b, c, d, e, f, matrix_color=(255, 255, 255), color=(0, 0, 0)):  # 说明书
        pygame.draw.rect(self.window, matrix_color, (0, 0, 1080, 720))
        text1 = self.font.render(a, True, color)
        text2 = self.font.render(b, True, color)
        text3 = self.font.render(c, True, color)
        text4 = self.font.render(d, True, color)
        text5 = self.font.render(e, True, color)
        text6 = self.font.render(f, True, color)

        # tw1, th1 = text1.get_size()
        # tx1 = bx1 + bw / 2 - tw1 / 2
        # ty1 = by1 + bh / 2 - th1 / 2
        self.window.blit(text1, (200, 0))
        self.window.blit(text2, (200, 50))
        self.window.blit(text3, (200, 100))
        self.window.blit(text4, (200, 150))
        self.window.blit(text5, (200, 200))
        self.window.blit(text6, (200, 250))
