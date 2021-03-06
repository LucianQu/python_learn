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
import sys  #使用模块sys退出游戏
import pygame # 包含开发游戏所需的功能

from src.chapter.alien_invasion.settings import Settings
from src.chapter.alien_invasion.ship import Ship
import src.chapter.alien_invasion.game_functions as gf #导入的模块gf指定别名gf
from pygame.sprite import Group #精灵编组
from src.chapter.alien_invasion.alien import Alien # 外星人
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
    ship = Ship(screen, play_setting) #创建一艘飞船
    bullets = Group() #创建一个用于存储子弹的编组 #Group实例

    #alien = Alien(play_setting, screen) # 创建一个外星人
    aliens = Group() #创建外星人编组
    gf.create_fleet(play_setting, screen, aliens, ship) #创建一群外星人
    while True:
        # 事件循环，侦听事件，根据事件发生的操作执行相应的任务，监视键盘和鼠标事件
        gf.check_events(play_setting, screen, ship, bullets)

        # 当你对编组调用update时，编组将自动对其中的每个精灵调用update（），因此代码行bullets.update()
        # 将为编组bullets中的每颗子弹调用bullet.update（）
        gf.update_ship(play_setting, ship)
        gf.update_bullets(bullets)
        gf.update_aliens(aliens)
        gf.update_screen(play_setting, screen, ship,aliens, bullets)  #更新屏幕

run_game() #运行游戏