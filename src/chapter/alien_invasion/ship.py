#!/user/bin/env python
# -*- coding:utf-8 -*-
"""**************************************************************************
*
*  File name: ship.py
*  Date: 2018/4/11 23:11
*  Copyright (c) 2013-2018 by Qulusheng.
*  Author: Lucian_qls
*  E-mail: 1017557706@qq.com
*
*  Function:
*   .飞船
*   Describe:
*   .负责管理飞船的大部分行为
* ChangeLog:
*   V1.0
**************************************************************************"""
import pygame
class Ship():
	def __init__(self, screen):
		"""* 初始化飞船并设置其初始位置 *"""
		self.screen = screen

		#加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#将每艘新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def blitme(self):
		"""* 在指定位置绘制飞船 *"""
		self.screen.blit(self.image, self.rect)