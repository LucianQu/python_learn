import requests
import re
import json
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36"
}  # 模拟手机


def get_num(url):
    response = requests.get(url, headers=headers).text
    print(str(response))
    result = re.search(
        r'&md5sum=(.*)&sign=(.*)&rtcs_flag=(.*)&rtcs_ver=(.*?)".*rsign":"(.*?)",', response, re.M | re.I)  # 寻找参数
    reader = {
        "md5sum": result.group(1),
        "sign": result.group(2),
        "rtcs_flag": result.group(3),
        "rtcs_ver": result.group(4),
        "width": 176,    
        "type": "org",
        "rsign": result.group(5)
    }

    result_page = re.findall(
        r'merge":"(.*?)".*?"page":(.*?)}', response)  # 获取每页的标签
    doc_url = "https://wenku.baidu.com/view/b12ff5a18462caaedd3383c4bb4cf7ec4afeb69e?fr=sogou&_wkts_=1668521533825"  # 网页的前缀
    n = 0
    for i in range(len(result_page)):  # 最大同时一次爬取10页
        if i % 10 is 0:
            doc_range = '_'.join([k for k, v in result_page[n:i]])
            reader['pn'] = n + 1
            reader['rn'] = 10
            reader['callback'] = 'sf_edu_wenku_retype_doc_jsonp_%s_10' % (
                reader.get('pn'))
            reader['range'] = doc_range
            n = i
            get_page(doc_url, reader)
    else:  # 剩余不足10页的
        doc_range = '_'.join([k for k, v in result_page[n:i + 1]])
        reader['pn'] = n + 1
        reader['rn'] = i - n + 1
        reader['callback'] = 'sf_edu_wenku_retype_doc_jsonp_%s_%s' % (
            reader.get('pn'), reader.get('rn'))
        reader['range'] = doc_range
        get_page(doc_url, reader)


def get_page(url, data):
    response = requests.get(url, headers=headers, params=data).text
    response = response.encode(
        'utf-8').decode('unicode_escape')  # unciode转为utf-8 然后转为中文
    response = re.sub(r',"no_blank":true', '', response)  # 清洗数据
    result = re.findall(r'c":"(.*?)"}', response)  # 寻找文本匹配
    result = '\n'.join(result)
    print("结果 "+result)

if __name__ == '__main__':
    #url = "https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html"
    # url = "https://wenku.baidu.com/view/3e1bb7c3fad6195f302ba6c8.html?rec_flag=default&sxts=1562641356908"
    url = "https://wenku.baidu.com/view/b12ff5a18462caaedd3383c4bb4cf7ec4afeb69e?fr=sogou&_wkts_=1668521533825"
    get_num(url)