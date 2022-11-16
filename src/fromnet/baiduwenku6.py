
import requests
import re

# 设置会话列表
session = requests.session()
# 请求网址
def get_content_url(url):
    return session.get(url).content.decode('utf-8')

def main():
    url = requests.get("https://wenku.baidu.com/view/b12ff5a18462caaedd3383c4bb4cf7ec4afeb69e?fr=sogou&_wkts_=1668521533825").url
    content = get_content_url(url)
    print(str(content))
