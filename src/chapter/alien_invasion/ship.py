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
	# 接收两个参数：引用self和screen，其中后者指定了要将飞船绘制到什么地方
	def __init__(self, screen):
		"""* 初始化飞船并设置其初始位置 *"""
		self.screen = screen

		#加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect() #获取image（surface）的属性rect，处理游戏元素就像能够处理矩形（rect对象），即便他们的形状并非矩形
		#之所以高效是因为矩形是简单的几何形状。游戏玩家几乎注意不到我们处理的不是游戏元素的实际形状。
		#处理rect对象时，可使用矩形四角和中心x和y坐标。可通过设置这些值来指定矩形的位置
			#居中：center、centerx（中心x坐标）或centery（中心y坐标）
			#屏幕边缘对齐：top、bottom、left或right
			#调整元素的水平或者垂直位置，可使用属性x和y（矩形左上角的x和y坐标）
			#原点（0,0）位于屏幕左上角，游戏中右下角的坐标（1200,800）
		self.screen_rect = screen.get_rect()

		#将每艘新飞船放在屏幕底部中央
			#注意center必须接收center，centerx和centery亦如此
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def blitme(self):
		"""* 在指定位置绘制飞船 *"""
		self.screen.blit(self.image, self.rect) #图像绘制在屏幕上