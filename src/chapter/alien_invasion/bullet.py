#!/user/bin/env python
# -*- coding:utf-8 -*-
"""**************************************************************************
*
*  File name: bullet.py
*  Date: 2018/4/13 23:57
*  Copyright (c) 2013-2018 by Qulusheng.
*  Author: Lucian_qls
*  E-mail: 1017557706@qq.com
*
*  Function:
*   .子弹类
*   Describe:
*   .飞船发射的子弹的管理类
* ChangeLog:
*   V1.0
**************************************************************************"""
import pygame
from pygame.sprite import Sprite #使用精灵，将游戏中相关的元素编组，同时操作编组中的所有元素

class Bullet(Sprite):
	"""* 一个对飞船发射的子弹进行管理的类 *"""
	#传入游戏设置，屏幕信息和飞船实例
	def __init__(self, play_settings, screen, ship):
		"""* 在飞船所处的位置创建一个子弹对象 *"""
		#继承Sprite，使用了python2.7语法，也适用3，可简写super().__init__()
		super(Bullet, self).__init__()
		self.screen = screen

		#在（0,0）处创建一个表示子弹的矩形，再设置正确的位置
		#创建空白矩形，提供矩形左上角xy坐标和长和宽
		self.rect = pygame.Rect(0, 0, play_settings.bullet_width, play_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		#存储用小数表示的子弹位置
		self.y = float(self.rect.y)

		self.color = play_settings.bullet_color
		self.speed_factor = play_settings.bullet_speed_factor
	def update(self):
		"""* 向上移动子弹 *"""
		#更新表示子弹位置的小数值
        # 当你对编组调用update时，编组将自动对其中的每个精灵调用update（），因此代码行bullets.update()
        #将为编组bullets中的每颗子弹调用bullet.update（）
		self.y -= self.speed_factor
		#更新表示子弹的rect的位置
		self.rect.y = self.y

	def draw_bullet(self):
		"""* 在屏幕上绘制子弹 *"""
		pygame.draw.rect(self.screen, self.color, self.rect)

