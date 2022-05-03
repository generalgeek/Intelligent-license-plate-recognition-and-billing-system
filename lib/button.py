import pygame


# 自定义按钮
class Button:
    """msg为要在按钮中显示的文本"""

    def __init__(self, screen: pygame.surface, centerxy, width, height, btn_color, text_color, msg,
                 size):
        self.screen = screen
        self.width, self.height = width, height
        self.btn_color, self.text_color = btn_color, text_color
        self.font = pygame.font.SysFont('SimHei', size)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # 用来存储矩形坐标的对象
        self.rect.centerx = centerxy[0] - self.width / 2 + 2
        self.rect.centery = centerxy[1] - self.height / 2 + 2
        self.deal_msg(msg)

    def deal_msg(self, msg):
        self.msg_img = self.font.render(msg, True, self.text_color, self.btn_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.btn_color, self.rect)
        # 将图像绘制到屏幕
        self.screen.blit(self.msg_img, self.msg_img_rect)
