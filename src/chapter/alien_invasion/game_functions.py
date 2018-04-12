"""**************************************************************************
*
*  File name: game_functions.py
*  Date: 2018/4/12 20:01
*  Copyright (c) 2013-2018 by Qulusheng.
*  Author: Lucian_qls
*  E-mail: 1017557706@qq.com
*
*  Function:
*   .存储游戏的运行函数
*  Describe:
*   .避免alien_invasion太长，并使其逻辑更容易理解
* ChangeLog:
* V1.0
**************************************************************************"""
import sys
import pygame

def check_events():
    """* 响应按键和鼠标事件 *"""
    for event in pygame.event.get():
        # pygame检测到的事件，所有键盘和鼠标事件都将促使for循环运行
        # 编写一系列if语句来检测并响应特定事件，点击关闭则检测到pygame.QUIT
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(play_setting, screen, ship):
    # 每次循环时都重绘屏幕
    screen.fill(play_setting.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见,移动元素时要不停的更新屏幕，显示新元素的位置，并在原来的位置隐藏元素，从而营造平滑效果
    pygame.display.flip()

