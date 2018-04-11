"""**************************************************************************
*
*  File name: alien_invasion.py
*  Date: 2018/4/11 19:23
*  Copyright (c) 2013-2018 by Qulusheng.
*  Author: Lucian_qls
*  E-mail: 1017557706@qq.com
*
*  Function:
*   .创建Pygame窗口以及响应用户输入
 * ChangeLog:
 * V1.0
**************************************************************************"""
import sys #使用模块sys退出游戏
import pygame # 包含开发游戏所需的功能

from src.chapter.alien_invasion.settings import Settings
from src.chapter.alien_invasion.ship import Ship

"""
1、pygame默认加载位图(.bmp)
2、选择背景透明的图像，可用图像编辑器将背景设置为任何掩饰
"""
def run_game():
    # 初始化背景设置
    pygame.init()

    play_setting = Settings() ; #创建Setting实例,存储在变量游戏设置中

    # 初始化屏幕， screen是一个surface
    # 在游戏中每个元素（外星人）都是一个surface，display.set_mode()返回的surface表示整个游戏窗口。我们激活
    # 游戏的动画循环后，每经过一次循环都将自动重绘这个surface
    screen = pygame.display.set_mode((play_setting.screen_width, play_setting.screen_height))  #argument 1 must be 2-item sequence, not int
    pygame.display.set_caption(play_setting.game_title)

    #创建一艘飞船
    ship = Ship(screen)
    # 开始游戏的主循环
    while True:
        # 事件循环，侦听事件，根据事件发生的操作执行相应的任务，监视键盘和鼠标事件
        for event in pygame.event.get():
            # pygame检测到的事件，所有键盘和鼠标事件都将促使for循环运行
            #编写一系列if语句来检测并响应特定事件，点击关闭则检测到pygame.QUIT
            if event.type == pygame.QUIT:
                sys.exit()

        #每次循环时都重绘屏幕
        screen.fill(play_setting.bg_color)

        ship.blitme()

        # 让最近绘制的屏幕可见,移动元素时要不停的更新屏幕，显示新元素的位置，并在原来的位置隐藏元素，从而营造平滑效果
        pygame.display.flip()

run_game() #运行游戏