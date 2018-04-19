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
from src.chapter.alien_invasion.alien import  Alien
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
        fire_bullet(play_settings, screen, ship, bullets)
    elif event_key == pygame.K_q:
        sys.exit()

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
def update_screen(play_setting, screen, ship,aliens, bullets):
    #删除超出界面的子弹
    delete_bullet(bullets)

    # 每次循环时都重绘屏幕
    screen.fill(play_setting.bg_color)
    ship.update_image()
    #降低长按键时，飞船移动速度
    if play_setting.num < play_setting.max_num:
        play_setting.num += 1
    else:
        ship.update(play_setting)
        play_setting.num = 0

    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen) # 编组调用draw时，pygame自动绘制编组的每个元素，绘制位置由元素的属性决定

    # 让最近绘制的屏幕可见,移动元素时要不停的更新屏幕，显示新元素的位置，并在原来的位置隐藏元素，从而营造平滑效果
    pygame.display.flip()
"""
删除超出屏幕的子弹
"""
def delete_bullet(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets)) #将输出写入到终端花费的时间比将图形绘制到游戏窗口花费的时间还要多
"""
发射子弹
"""
def fire_bullet(play_settings, screen, ship, bullets):
    """* 如果没有达到限制，就发射一颗子弹 *"""
    #创建新子弹，并将其加入到编组bullets中
    if len(bullets) < play_settings.bullets_allowed:
        new_bullet = Bullet(play_settings, screen, ship)
        bullets.add(new_bullet)

"""
创建外星人群
"""
def create_fleet(play_settings, screen, aliens):
    """* 创建外星人群 *"""
    alien = Alien(play_settings, screen)
    number_aliens_x = get_number_aliens_x(play_settings, alien.rect.width)   #int确保外星人的数量为整数

    #创建第一行外星人
    for alien_number in range(number_aliens_x):
        create_alien(play_settings, screen, aliens, alien_number) #创建一个外星人
"""
获取一行能容纳多少个外星人
"""
def get_number_aliens_x(play_setting, alien_width):
    """* 计算每行可容纳多少个外星人 *"""
    available_space_x = play_setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
"""
创建一个外星人
"""
def create_alien(play_settings, screen, aliens, alien_number):
    # 创建一个外星人并将其加入当前行
    alien = Alien(play_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)