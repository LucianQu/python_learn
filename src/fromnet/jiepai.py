import re
import json
import time
import random

from pathlib import Path
from urllib import parse
from urllib import error
from urllib import request
import requests
from datetime import datetime
from http.client import IncompleteRead
from socket import timeout as socket_timeout
import urllib
import codecs
from bs4 import BeautifulSoup


def _get_timestamp():
    """
    向 http://www.toutiao.com/search_content/ 发送的请求的参数包含一个时间戳，
    该函数获取当前时间戳，并格式化成头条接收的格式。格式为 datetime.today() 返回
    的值去掉小数点后取第一位到倒数第三位的数字。
    """
    row_timestamp = str(datetime.timestamp(datetime.today()))
    return row_timestamp.replace('.', '')[:-3]


def _create_dir(name):
    """
    根据传入的目录名创建一个目录，这里用到了 python3.4 引入的 pathlib 库。
    """
    directory = Path(name)
    #directory1 = re.sub(r'[\/:*?"<>|]', " ", directory)  # 替换为下划线
    if not directory.exists():
        #dir_name = re.sub(r'[\\\r\n]', '', directory)
        directory.mkdir()
    return directory

def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title

def _get_query_string(data):
    """
    将查询参数编码为 url，例如：
    data = {
            'offset': offset,
            'format': 'json',
            'keyword': '街拍',
            'autoload': 'true',
            'count': 20,
            '_': 1480675595492
    }
    则返回的值为：
    ?offset=20&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&_=1480675595492"
    """
    # print(parse.urlencode(data))
    return parse.urlencode(data)


def get_article_urls(req, timeout=20):
    with request.urlopen(req, timeout=timeout) as res:
        d = json.loads(res.read().decode()).get('data')

        if d is None:
            print("数据全部请求完毕...")
            return

        urls = [article.get('article_url') for article in d if article.get('article_url')]
        return urls


def get_photo_urls(req, timeout=20):

    with request.urlopen(req, timeout=timeout) as res:  # res = html
        # print(res)
        # 这里 decode 默认为 utf-8 编码，但返回的内容中含有部分非 utf-8 的内容，会导致解码失败
        # 所以我们使用 ignore 忽略这部分内容
        # print("***********************************************************")
        # soup = BeautifulSoup(res.read().decode(errors='ignore'), 'html5lib')
        soup = BeautifulSoup(res.read().decode(errors='ignore'), 'html.parser')
        # print(soup)
        # article_main = soup.find('var', id='article-main')
        # print(soup.prettify())
        #scripts = soup.find_all("script")
        # print(scripts)

        # //p
        # &quot  '//p. + \.&quot'
        # list_url = re.search(r"\//.*\&quot", soup)

        # list_url = re.search(r"\//.*\&quot", soup)
        # print(list_url)
        title_article = ""
        if soup.select('title'):
            title_article = str(soup.select('title')[0].get_text)
            if len(title_article) > 36:
                title_article = title_article[36:-9]
        list_img = []
        for tag in soup.find_all(re.compile("script")):

            # print(tag)
            # print("^^^^^^^^^^^^^^^^^^^^^^1^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            # print(tag.string)
            var_BASE_DATA = tag.string
            if var_BASE_DATA:
                if "var BASE_DATA" in var_BASE_DATA:
                    # r = re.compile(r'\//p.*\&quot')
                    r = re.compile(r'(//p.*?\&quot)')
                    # print(r.findall(var_BASE_DATA))
                    list = r.findall(var_BASE_DATA)

                    for l in list:
                        # print(l)
                        list_img.append("https://" + l[2:-5])
                    # print(list_img)
                    print(True)

            # print("^^^^^^^^^^^^^^^^^^^^^^2^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            # print(tag.contents)
        return title_article, list_img
        key_text = "var BASE_DATA"
        # article = soup.find(["script", "style"])
        # article = soup.find('div', class_='article-box')
        # dict_list = json.loads(urllib.request.urlopen(req).)
        # print(dict_list)
        return

        # article = soup.find_all('script')
        # print(article)
        # if len(article) >=1:
        # #     title = article_info[0]['title'].get_text
        #      print(article)

        # if len() >= 1:
        #     title = soup.select('title')[0].get_text
        #     print(title)
        contents = soup.select('content')
        if len(contents) >= 1:
            print(contents)

        images_pattern = re.compile(r'gallery: (.*?),\n')
        result = re.search(images_pattern, res.read().decode(errors='ignore'))
        if result:
            # 将json数据转换为python的字典对象
            data = json.loads(result.group(1))
            if data and 'sub_images' in data.keys():
                print("yes")
                return
            else:
                print("error")

        article_main = soup.find(name="article-box")

        if not article_main:
            print("无法定位到文章主体...")
            return

        heading = article_main.h1.string

        if '街拍' not in heading:
            print("这不是街拍的文章！！！")
            return

        img_list = [img.get('src') for img in article_main.find_all('img') if img.get('src')]
        return heading, img_list


def save_photo(photo_url, save_dir, timeout=20):
    photo_name = photo_url.rsplit('/', 1)[-1] + '.jpg'

    # 这是 pathlib 的特殊操作，其作用是将 save_dir 和 photo_name 拼成一个完整的路径。例如：
    # save_dir = 'E：\jiepai'
    # photo_name = '11125841455748.jpg'
    # 则 save_path = 'E：\jiepai\11125841455748.jpg'
    save_path = save_dir / photo_name

    with request.urlopen(photo_url, timeout=timeout) as res, save_path.open('wb') as f:
        f.write(res.read())
        print('已下载图片：{dir_name}/{photo_name}，请求的 URL 为：{url}'
              .format(dir_name=dir_name, photo_name=photo_name, url=a_url))


def get_page_index(offset, keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab'
    }
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    }
    try:
        response = requests.get(url='https://www.toutiao.com/search_content', params=data, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except :
        print('请求索引页错误')
        return None
        pass
def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            if item and 'article_url' in item.keys():
                yield item.get('article_url')

            def get_page_detail(url):
                try:
                    response = requests.get(url)
                    # response.encoding = response.apparent_encoding
                    if response.status_code == 200:
                        return response.text
                    return None
                except :
                    print('请求详情页错误', url)
                    return None
                    pass

def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    print('title:', title)
    images_pattern = re.compile(r'gallery: JSON.parse\("(.*?)"\),', re.S)
    result = re.search(images_pattern, html)
    if result:
        # group(0)是原始字符串, group(1)是第一个括号匹配到的字符串
        # groups()以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)
        # codecs: 使不具有转义的反斜杠具有转义功能
        data_str = codecs.getdecoder('unicode_escape')(result.group(1))[0]
        json_data = json.loads(data_str)
        if json_data and 'sub_images' in json_data.keys():
            sub_images = json_data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images:
                download_image(image)
            return {
                'title': title,
                'images': images,
                'url': url
            }
    else:
        print('没有搜索到符合条件的gallery数据', end='\n\n')

def download_image(url):
    print('正在下载图片', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content)
    except :
        print('请求图片错误', url)
        pass

#def main(offset):
#html = get_page_index(offset, KEYWORD)
#for url in parse_page_index(html):
#detail_html = get_page_detail(url)

if __name__ == '__main__':
    ongoing = True
    offset = 0  # 请求的偏移量，每次累加 20
    root_dir = _create_dir('D:\\jiepai')  # 保存图片的根目录
    request_headers = {
        'Referer': 'http://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/54.0.2840.99 Safari/537.36'
    }

    while ongoing:
        timestamp = _get_timestamp()
        query_data = {
            'offset': offset,
            'format': 'json',
            'keyword': '街拍',
            'autoload': 'true',
            'count': 1,  # 每次返回 20 篇文章
            '_': timestamp
        }
        query_url = 'http://www.toutiao.com/search_content/' + '?' + _get_query_string(query_data)
        print(query_url)
        article_req = request.Request(query_url, headers=request_headers)
        article_urls = get_article_urls(article_req)

        # 如果不再返回数据，说明全部数据已经请求完毕，跳出循环
        if article_urls is None:
            break

        # 开始向每篇文章发送请求
        for a_url in article_urls:
            # 请求文章时可能返回两个异常，一个是连接超时 socket_timeout，
            # 另一个是 HTTPError，例如页面不存在
            # 连接超时我们便休息一下，HTTPError 便直接跳过。
            try:
                photo_req = request.Request(a_url, headers=request_headers)
                photo_urls = get_photo_urls(photo_req)

                # 文章中没有图片？跳到下一篇文章
                if photo_urls is None:
                    continue

                article_heading, photo_urls = photo_urls

                # 这里使用文章的标题作为保存这篇文章全部图片的目录。
                # 过滤掉了标题中在 windows 下无法作为目录名的特殊字符。
                dir_name = re.sub(r'[\\/\-：*?"<>|\\\r\\\n]', '', article_heading)
                download_dir = _create_dir(root_dir / dir_name)

                # 开始下载文章中的图片
                for p_url in photo_urls:
                    # 由于图片数据以分段形式返回，在接收数据时可能抛出 IncompleteRead 异常
                    try:
                        save_photo(p_url, save_dir=download_dir)
                    except IncompleteRead as e:
                        print(e)
                        continue
            except socket_timeout:
                print("连接超时了，休息一下...")
                time.sleep(random.randint(15, 25))
                continue
            except error.HTTPError:
                continue

        # 一次请求处理完毕，将偏移量加 20，继续获取新的 20 篇文章。
        offset += 1

