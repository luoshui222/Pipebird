import pygame


class Bird:
    def __init__(self,window):
        self.window = window


        self.birdY = 350  # 鸟所在Y轴坐标,即上下飞行高度

        self.jump = False  # 默认情况小鸟自动降落
        self.jumpSpeed = 65  # 跳跃高度
        self.gravity = 6  # 重力
        self.dead = False  # 默认小鸟生命状态为活着

    def birdUp(self):
        # 小鸟跳跃
        self.birdY -= self.jumpSpeed  # 鸟Y轴坐标减小，小鸟上升
    def getbird(self):
        birdStatus = pygame.image.load("files/dingzhen.jpg")
        new = pygame.transform.rotozoom(birdStatus, 0, 0.05)
        self.window.blit(new, (120, self.birdY))
        # self.birdRect = pygame.Rect(self.birdX, self.birdY, 36, 45)  # 鸟的矩形

    def birdDown(self):
        self.birdY += self.gravity
    def getrect(self):
        birdRect = pygame.Rect(120, self.birdY, 36, 45)
        return birdRect