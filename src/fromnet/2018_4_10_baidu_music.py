import requests
from bs4 import BeautifulSoup
import re


def get_one_page(url):
    wb_data = requests.get(url)
    wb_data.encoding = wb_data.apparent_encoding
    if wb_data.status_code == 200:
        return wb_data.text
    else:
        return None


def parse_one_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.select('div.ranklist-wrapper.clearfix div.bd ul.song-list li')
    pattern1 = re.compile(
        r'<li.*?<div class="index">(.*?)</div>.*?title="(.*?)".*?title="(.*?)".*?</li>',
        re.S)
    pattern2 = re.compile(
        r'<li.*?<div class="index">(.*?)</div>.*?title="(.*?)".*?target="_blank">(.*?)</a>',
        re.S)

    wants = []
    for item in data:
        # print(item)
        final = re.findall(pattern1, str(item))
        if len(final) == 1:
            # print(final[0])
            wants.append(final[0])
        else:
            other = re.findall(pattern2, str(item))
            # print(module[0])
            wants.append(other[0])
    return wants


if __name__ == '__main__':
    url = 'http://music.baidu.com/'
    html = get_one_page(url)
    data = parse_one_page(html)
    for item in data:
        dict = {
            '序列': item[0],
            '歌名': item[1],
            '歌手': item[2]
        }
        print(dict)