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
	def __init__(self, screen, play_settings):
		"""* 初始化飞船并设置其初始位置 *"""
		self.screen = screen
		self.play_settings = play_settings #飞船游戏设置

		#加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship7.bmp')
		self.image_type = 0 #飞船图标标志
		self.image_update = False #是否更新飞船图标

		self.rect = self.image.get_rect() #获取image（surface）的属性rect，处理游戏元素就像能够处理矩形（rect对象），即便他们的形状并非矩形
		self.half_width = self.rect.width / 2
		self.half_height = self.rect.height / 2
		self.height = self.rect.height
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

		#centerx属性只能存储整数值，故用center
		self.center = float(self.rect.centerx) #在飞船的属性center中存储小数值

		#玩家右键不放时，我们希望飞船不断向右移动，知道玩家松开为止。需要检测KEYUP和KEYDOWN和moving_right标志
		#飞船不动时，标志moving_right为false，右键按下时，标志位true，而玩家松开时置为false

		# 向右移动标志
		self.moving_right = False
		# 向左移动标志
		self.moving_left = False
		# 向下移动标志
		self.moving_down = False
		# 向上移动标志
		self.moving_up = False
	"""
	更新飞船图标
	"""
	def update_image(self):
		if self.image_type == 1 and self.image_update:# 按下1，切换鼻涕糖号
			self.image = pygame.image.load('images/ship5.bmp')
		elif self.image_type == 2 and self.image_update:# 按下2，切换脆糖号
			self.image = pygame.image.load('images/ship4.bmp')
		elif self.image_type == 3 and self.image_update:# 按下3，切换玉米糖号
			self.image = pygame.image.load('images/ship3.bmp')
		elif self.image_type == 4 and self.image_update:# 按下4，切换酥糖号
			self.image = pygame.image.load('images/ship2.bmp')
		elif self.image_type == 5 and self.image_update:# 按下5，切换扫地僧号
			self.image = pygame.image.load('images/ship6.bmp')
		if self.image_update:
			# self.rect = self.image.get_rect()  # 获取image（surface）的属性rect，处理游戏元素就像能够处理矩形（rect对象），即便他们的形状并非矩形
			# self.half_width = self.rect.width / 2
			# self.half_height = self.rect.height / 2
			# self.height = self.rect.height
			# self.rect.centerx = self.screen_rect.centerx
			# self.rect.bottom = self.screen_rect.bottom
			self.image_update = False

	"""
	屏幕绘制飞船
	"""
	def blitme(self):
		"""* 在指定位置绘制飞船 *"""
		self.screen.blit(self.image, self.rect) #图像绘制在屏幕上
	"""
	更新飞船位置
	"""
	def update(self, settings):
		"""* 根据移动标志调整飞船的位置 *"""
		if self.moving_right:
			# 向右移动飞船
			if self.rect.centerx <= settings.screen_width- self.half_width:
				speed = self.rect.centerx
				speed += settings.ship_speed_factor
				self.rect.centerx = speed
		elif self.moving_left:
			#向左移动飞船
			if self.rect.centerx >= self.half_width:
				speed = self.rect.centerx
				speed -= settings.ship_speed_factor
				self.rect.centerx = speed
		elif self.moving_up:
			#向上移动飞船
			if self.rect.bottom >= self.height:
				speed = self.rect.bottom
				speed -= settings.ship_speed_factor
				self.rect.bottom = speed
		elif self.moving_down:
			#向下移动飞船
			if self.rect.bottom <= settings.screen_height:
				speed = self.rect.bottom
				speed += settings.ship_speed_factor
				self.rect.bottom = speed

		#根据self.center更新rect对象
		#self.rect.centerx = self.center #centerx只存储整数部分，由于不是计算阶段，误差小于1