import pygame
from random import randint



class Background:
    def __init__(self, window):
        self.window = window
        self.x = None
        self.y = None
        # self.xyRect = pygame.Rect(self.x, self.y, 45, 420)
        # self.xyRect = pygame.draw.rect(window,(120,20,60),(self.x,self.y,45,420))

    def background(self, window, scale_a=1.5, bx=1035, by=0):
        image1 = pygame.image.load('files/xiangyan.png')
        # 操作图片大小 获取图片的比例
        w, h = image1.get_size()
        # 缩放图片 可能会发生形变
        # new = pygame.transform.scale(image1, (1080, 720))
        new = pygame.transform.rotozoom(image1, 0, scale_a)  # rotozoom方法可以缩放比例 并且旋转多少度
        # 2 .渲染图片
        # blit（渲染对象 ，坐标）
        window.blit(new, (bx, by))
        # 3.刷新页面
        # pygame.display.update()
    def litang(self):
        image1 = pygame.image.load('files/litang.png')
        # 操作图片大小 获取图片的比例
        w, h = image1.get_size()
        # 缩放图片 可能会发生形变
        # new = pygame.transform.scale(image1, (1080, 720))
        new = pygame.transform.rotozoom(image1, 0, 0.95)  # rotozoom方法可以缩放比例 并且旋转多少度
        # 2 .渲染图片
        # blit（渲染对象 ，坐标）
        self.window.blit(new, (0, 0))


    def rebackground(self, window, scale_a=1.5, bx=1035, by=500):
        image1 = pygame.image.load('files/xiangyan.png')
        # 操作图片大小 获取图片的比例
        w, h = image1.get_size()
        # 缩放图片
        # new = pygame.transform.scale(image1, (1080, 720))
        new = pygame.transform.rotozoom(image1, 180, scale_a)
        # 2 .渲染图片
        # blit（渲染对象 ，坐标）
        window.blit(new, (bx, by))

    def randomBackground(self, bx, by):
        self.x = bx
        self.y = by
        self.background(self.window, scale_a=1.5, bx=bx, by=by)
        # background2 = Background()
        self.rebackground(self.window, scale_a=1.5, bx=bx, by=by + 550)

    def getby(self):
        return randint(-250, 0)

    def getrect(self):
        xyRect = pygame.Rect(self.x, self.y, 42, 400)
        return xyRect

    def getrerect(self):
        xyRect = pygame.Rect(self.x, self.y + 550, 42, 400)
        return xyRect
    def getX(self):
        return self.x




