"""****************-*******************"""
# describe: 获取豆瓣电影列表，保存json中
# author  : qulus
# time    : 2017/11/8 0008 9:05
"""****************-*******************"""
import requests
import json

class Douban(object):
    def __init__(self):
        self.url = "https://m.douban.com/rexxar/api/v2/subject_collection" \
                   "/movie_showing/items?&start=0&count=100"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit'
                          '/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 '
                          'Safari/537.36'
        }

    def get_data(self):
        response = requests.get(self.url, headers = self.headers)
        print(response.content.decode())
        return response.content.decode('UTF-8')

    def parse_data(self, data):
        print(type(data))
        dict_data = json.loads(data)

        # 使用key获取值，movie_list是一个元素为字典的列表
        movie_list = dict_data['subject_collection_items']

        # 把提取的内容放到新的元素为字典(key电影名称)的列表中
        data_list = []

        for movie_info in movie_list:
            temp_dict = {}
            temp_dict['title'] = movie_info['title']
            temp_dict['url'] = movie_info['url']
            data_list.append(temp_dict)
        return data_list


    def save_data(self, data_list1):
        with open('douban_movice.json', 'w') as f:
            for data_info in data_list1:
                str_data = json.dumps(data_info, ensure_ascii=False) + ',\n'
                f.write(str_data)

    def run(self):
        # 发起请求
        data = self.get_data()

        # 解析数据
        data_result = self.parse_data(data)

        # 保存数据
        self.save_data(data_result)
#  python文件有两种使用方法：
#   1.作为脚本  2.import 到其他python脚本中被调用执行，模块重用
#  在if __name__ == 'main': 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行
#  而import到其他脚本中是不会被执行的，能执行 if之前的语句
"""
原理：
    每个python模块都包含内置的变量 __name__，当运行模块被执行的时候， __name__等于文件名(包含后缀)
    如果import到其他模块中，则__name__等于模块名称（不包含后缀）,而__main__等于当前执行文件的
    名称(包含后缀)，进而当模块被直接执行时，__name__ == "__main__"，结果为真
    __main__就是一个字符串而已，__name__是内置变量在直接执行时等于__main__
    src.other.class_dog
    文件__name__变量：
        1.当前文件执行时为__main__
        2.导入其他包时，为包路径不加后缀

"""

print(__name__)
if __name__ == "__main__":

    douban = Douban()
    douban.run()
