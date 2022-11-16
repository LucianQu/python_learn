# -*- codeing=utf-8 -*-
# @Time:2021/7/30 12:06
# @Atuhor:@lwtyh
# @File:demo.py
# @Software:PyCharm

import time

from docx import Document  # 需要安装第三方库python-docx
from docx.oxml.ns import qn  # 中文格式
from docx.shared import Pt  # 用于设置字体样式
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from bs4 import BeautifulSoup

# driver = webdriver.Chrome(r'D:\pythonproject\36\git_test\python_learn\src\fromnet\chromedriver.exe')
option = webdriver.ChromeOptions()
option.binary_location=r'D:\pythonproject\36\git_test\python_learn\src\fromnet\chromedriver.exe'
driver = webdriver.Chrome()

driver.get("https://wenku.baidu.com/view/b12ff5a18462caaedd3383c4bb4cf7ec4afeb69e?fr=sogou&_wkts_=1668521533825")
html = driver.page_source
bf1 = BeautifulSoup(html,'lxml')
# print(bf1.prettify())
print(bf1.getText())
test_list =''
list_div = bf1.find_all('div', class_='content singlePage wk-container')
for list_p in list_div:
    text = list_p.get_text()
    test_list +=text

docx_path = "课程设计.docx"
doc = Document()
doc.styles["Normal"].font.name = u"宋体"  # 设置字体样式
doc.styles["Normal"].font.size = Pt(14)  # 设置字体大小
doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')  # 设置文档的基础样式
doc.add_paragraph(str(test_list))  # 增加一个paragraph,写入内容
doc.save(r"D:\test.docx")