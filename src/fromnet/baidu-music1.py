import sys, os
import urllib
import urllib.request as urllib2
import importlib
import urllib.parse
from bs4 import BeautifulSoup
import json
from multiprocessing import Process
import codecs

class BaiDuMusic():
    def __init__(self):
        importlib.reload(sys)
        # fopen = codecs.open('file_name.txt', 'r', 'UTF-8')
    def search(self, songName):
        firstUrl = "http://music.baidu.com/search?key=" + urllib.parse.unquote(str(songName))
        userAgent = " User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)" \
                    " Chrome/39.0.2171.71 Safari/537.36 "
        headers = {'User-Agent': userAgent}
        requst = urllib2.Request(firstUrl, headers=headers)
        result = urllib2.urlopen(requst).read()

        # 使用BeautifulSoup快速解析html文档
        soup = BeautifulSoup(result, from_encoding="utf-8")
        res_arr = []
        try:
            tmpjson = soup.find_all("li", {"class": "bb-dotimg clearfix song-item-hook "})
            for x in tmpjson:
                tmpobj = json.loads(x['data-songitem'])
                value =tmpobj['songItem']['oid'] + "+++" + tmpobj['songItem']['author'] + "+++" + tmpobj['songItem']['sname'][
                                                            4:-5]
                res_arr.append(value)
            return res_arr
        except Exception:
            print ("抱歉没有找到相关资源")
            return 0

    def download(self, songid, songName, savePath="down/"):
        songNewUrl = "http://music.baidu.com/song/" + str(songid)
        if not os.path.isdir(savePath):
            os.makedirs(savePath)
        savemp3 = savePath + songName + ".mp3"
        urllib.request.urlretrieve(songNewUrl, savemp3)


if __name__ == '__main__':
    bMusic = BaiDuMusic()
    # res = bMusic.search("Federale")
    # for x in res:
    # print x
    # 1128053+++刘德华+++冰雨
    # 7327899+++李翊君+++冰雨
    # 53535187+++张恒+++冰雨
    # Process(target=bMusic.download, args=(1128053, "刘德华-冰雨")).start()
    Process(target=bMusic.download, args=(541816852, "爱情路口")).start()
    # Process(target=bMusic.download, args=(53535187, "张恒-冰雨")).start()