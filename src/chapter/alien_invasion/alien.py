"""**************************************************************************
*
*  File name: alien.py
*  Date: 2018/4/18 19:46
*  Copyright (c) 2013-2018 by Qulusheng.
*  Author: Lucian_qls
*  E-mail: 1017557706@qq.com
*
*  Function:
*   .外星人类
*  Describe:
*   .飞船要打的外星人
* ChangeLog:
* V1.0
**************************************************************************"""

import  pygame
from pygame.sprite import  Sprite

class Alien(Sprite):
    """* 表示单个外星人的类 *"""
    def __init__(self, play_settings, screen):
        """* 初始化外星人并设置其起始位置 *"""
        super(Alien, self).__init__()
        self.screen = screen
        self.play_settings = play_settings

        #加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width  #外星人的左边距设置为外星人宽度
        self.rect.y = self.rect.height #外星人的上边距设置为外星人的高度

        #存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """* 在指定位置绘制外星人 *"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """* 向右移动外星人 *"""
        self.x += self.play_settings.alien_speed_factor
        self.rect.x = self.x