from urllib.request import urlopen
import json


# 用json形式从豆瓣抓取电影的排行，通过审查元素找到看起来是json格式的链接

def get20Movie(url):
    html = urlopen(url)
    htmlJsonString = html.read()
    jsonObj = json.loads(htmlJsonString.decode())  # decode()很关键
    movieNameAndScores = []
    for each in jsonObj.get('subjects'):
        movieNameAndScores.append(" 电影名：" + each.get('title')
                                  + " 评分" + each.get('rate')
                                  + " URL:" + each.get('url'))
        # print(each.get('title')+each.get('rate'))
    return movieNameAndScores

file_lines = []
def save(file_lines):
    with open("movice.txt", 'w') as movice_content:
        for content in file_lines:
            movice_content.write( content + "      男主角：Qu Lu Sheng" + "\n")
        movice_content.closed

j = 0
i = 0  # 不能在def前面定义本文件的全局变量，模块中用global
while 1:
    movieNameAndScores = get20Movie(
        'https://movie.douban.com/j/search_subjects?'
        'type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_'
        'limit=20&page_start=' + str(
            j))
    for each in movieNameAndScores:
        print(str(i) + each)
        file_lines.append(each)
        i += 1
        if i >= 277:
            save(file_lines)
            break
    j += 20
