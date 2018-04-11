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

def run_game():
    # 初始化背景设置
    pygame.init()
    # 初始化屏幕， screen是一个surface
    # 在游戏中每个元素（外星人）都是一个surface，display.set_mode()返回的surface表示整个游戏窗口。我们激活
    # 游戏的动画循环后，每经过一次循环都将自动重绘这个surface
    screen = pygame.display.set_mode((1200, 800))  #argument 1 must be 2-item sequence, not int
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game() #运行游戏