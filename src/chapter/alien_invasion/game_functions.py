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
from src.chapter.alien_invasion.bullet import Bullet

"""
用户操作监听/处理
"""
def check_events(play_settings, screen, ship, bullets):
    """* 响应按键和鼠标事件 *"""
    for event in pygame.event.get():
        # pygame检测到的事件，所有键盘和鼠标事件都将促使for循环运行
        # 编写一系列if语句来检测并响应特定事件，点击关闭则检测到pygame.QUIT
        if event.type == pygame.QUIT:#事件类型为退出
            sys.exit()
        elif event.type == pygame.KEYDOWN:#事件类型为键按下
            key_down_event(play_settings, screen, ship, event.key, bullets)
        elif event.type == pygame.KEYUP:  # 事件类型为键按下
            key_up_event(ship, event.key)

"""
按键按下
"""
def key_down_event(play_settings, screen, ship, event_key, bullets):
    if event_key == pygame.K_RIGHT:  # 键为右键
        # 向右移动飞船开始
        ship.moving_right = True
    elif event_key == pygame.K_LEFT:  # 键为左键
        # 向左移动飞船开始
        ship.moving_left = True
    elif event_key == pygame.K_UP:  # 键为上键
        # 向上移动飞船开始
        ship.moving_up = True
    elif event_key == pygame.K_DOWN:  # 键为下键
        # 向下移动飞船开始
        ship.moving_down = True

    elif event_key == pygame.K_1: #键为1
        #切换飞船图片为鼻涕糖号
        ship.image_type = 1
        ship.image_update = True
    elif event_key == pygame.K_2:  # 键为2
        # 切换飞船图片为脆糖号
        ship.image_type = 2
        ship.image_update = True
    elif event_key == pygame.K_3:       # 切换飞船图片为玉米糖糖号
        ship.image_type = 3
        ship.image_update = True
    elif event_key == pygame.K_4:  # 键为4
        # 切换飞船图片为酥糖号
        ship.image_type = 4
        ship.image_update = True
    elif event_key == pygame.K_5:  # 键为5
        # 切换飞船图片为扫地僧糖号
        ship.image_type = 5
        ship.image_update = True
    elif event_key == pygame.K_0:
        # 切换飞船运行速度
        play_settings.ship_speed_factor += 0.5
    elif event_key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入到编组bullets中
        new_bullet = Bullet(play_settings, screen, ship)
        bullets.add(new_bullet)



"""
按键抬起
"""
def key_up_event(ship, type):
    if type == pygame.K_RIGHT:  # 键为右键
        # 向右移动飞船停止
        ship.moving_right = False
    elif type == pygame.K_LEFT:  # 键为左键
        # 向左移动飞船停止
        ship.moving_left = False
    elif type == pygame.K_UP:  # 键为上键
        # 向上移动飞船停止
        ship.moving_up = False
    elif type == pygame.K_DOWN:  # 键为下键
        # 向下移动飞船停止
        ship.moving_down = False

"""
更新屏幕
"""
def update_screen(play_setting, screen, ship, bullets):
    # 每次循环时都重绘屏幕
    screen.fill(play_setting.bg_color)
    ship.update_image()
    ship.update(play_setting)

    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    # 让最近绘制的屏幕可见,移动元素时要不停的更新屏幕，显示新元素的位置，并在原来的位置隐藏元素，从而营造平滑效果
    pygame.display.flip()

