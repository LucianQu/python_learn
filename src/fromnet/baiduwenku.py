# -*- codeing=utf-8 -*-
# @Time:2021/7/30 12:06
# @Atuhor:@lwtyh
# @File:demo.py
# @Software:PyCharm

import time

import requests
from docx import Document  # 需要安装第三方库python-docx
from docx.oxml.ns import qn  # 中文格式
from docx.shared import Pt  # 用于设置字体样式
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import parsel
import base64
# driver = webdriver.Chrome(r'D:\pythonproject\36\git_test\python_learn\src\fromnet\chromedriver.exe')
option = webdriver.ChromeOptions()
option.binary_location=r'D:\pythonproject\36\git_test\python_learn\src\fromnet\chromedriver.exe'
driver = webdriver.Chrome()

driver.get("https://wenku.baidu.com/view/b12ff5a18462caaedd3383c4bb4cf7ec4afeb69e?fr=sogou&_wkts_=1668521533825")

time.sleep(2)
driver.maximize_window()     # 自动将网页放大至最大化
# 为了避免百度页面变为旧版页面，需要刷新
driver.refresh()
time.sleep(2)
# # 点击登录
# account_login_button = driver.find_element(By.XPATH,'//div[@class="right-box"]/div[4]')
# account_login_button.click()
# # 账号密码登录
# time.sleep(2)
# account_login_button = driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__changePwdCodeItem"]')
# account_login_button.click()
#
# time.sleep(2)
# # 输入账号
# input_account = driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__userName"]')
# input_account.send_keys('1959073274@qq.com')
# time.sleep(2)
# # 输入密码
# input_password = driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__password"]')
# input_password.send_keys('www123456')
# time.sleep(2)
# # 点击登录按钮
# login_button = driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__submit"]')
# login_button.click()
#
# time.sleep(2)

# account_login_button = driver.find_element(By.NAME,'//div[@class="vcode-body vcode-body-spin"]/div[2]')        # 去掉验证
# account_login_button.click()
# 点击登录按钮（重新）
# time.sleep(2)
# login_button = driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__submit"]')
# login_button.click()
#
# time.sleep(2)
#
# account_login_button = driver.find_element(By.NAME,'//*[@id="app"]/div[3]/div[3]/div[4]/div/div[2]/i')        # 去掉广告
# account_login_button.click()


# time.sleep(2)
# driver.execute_script("window.scrollTo(0,4004)")  # 跳转到页面“阅读所有页面”的位置
# time.sleep(2)
# driver.find_element(By.NAME,"//div[@class='fold-page-text']").click()  # 点击“阅读所有页面“
# time.sleep(3)


driver.execute_script("window.scrollTo(0,400)")  # 跳转到页面初始位置

time.sleep(10)
#得到当前总页面
all_page = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[4]/div/div[1]/div[2]/div/div[1]/canvas').text
all_page = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[4]/div/div[1]/div[2]/div/div[1]/canvas').text
print(str(all_page))



