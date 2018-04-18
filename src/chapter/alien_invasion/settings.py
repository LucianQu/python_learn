#!/user/bin/env python
# -*- coding:utf-8 -*-
"""**************************************************************************
*
*  File name: settings.py
*  Date: 2018/4/11 21:37
*  Copyright (c) 2013-2018 by Qulusheng.
*  Author: Lucian_qls
*  E-mail: 1017557706@qq.com
*
*  Function:
*   .设置类
*   Describe:
*   .所有设置存储在这里，供程序调用
	.这个类只包含方法__init__()，初始化控制游戏外观和飞船速度的属性
* ChangeLog:
*   V1.0
**************************************************************************"""
class Settings():
	"""* 存储游戏所有设置的类 *"""
	def __init__(self):
        #游戏初始化设置
		#屏幕设置
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		self.game_title = "蛤蟆坑外五虎将"
		self.ship_speed_factor = 1.5
		#子弹设置
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 2

		self.num = 0
		self.max_num = 5
