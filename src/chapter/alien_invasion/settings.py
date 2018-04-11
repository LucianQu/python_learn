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
* ChangeLog:
*   V1.0
**************************************************************************"""
class Settings():
	"""* 存储游戏所有设置的类 *"""
	def __init__(self):
		"""* 初始化游戏的设置 *"""
		#屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		self.game_title = "扫地僧"