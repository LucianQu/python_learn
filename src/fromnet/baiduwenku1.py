import requests
import re
import json
import os

session = requests.session()


def fetch_url(url):
    return session.get(url).content.decode('utf-8')


def get_doc_id(url):
    if len(re.findall('view/(.*).html', url)) > 0:
        return re.findall('view/(.*).html', url)[0]
    else:
        print("id为空")


def parse_type(content):
    if len(re.findall(r"docType.*?\:.*?\'(.*?)\'\,", content)) > 0:
        return re.findall(r"docType.*?\:.*?\'(.*?)\'\,", content)[0]
    else:
        print("type为空")


def parse_title(content):
    if len(re.findall(r"title.*?\:.*?\'(.*?)\'\,", content)) > 0:
        return re.findall(r"title.*?\:.*?\'(.*?)\'\,", content)[0]
    else:
        print("title为空")


def parse_doc(content):
    result = ''
    url_list = re.findall('(https.*?0.json.*?)\\\\x22}', content)
    url_list = [addr.replace("\\\\\\/", "/") for addr in url_list]
    for url in url_list[:-5]:
        content = fetch_url(url)
        y = 0
        txtlists = re.findall('"c":"(.*?)".*?"y":(.*?),', content)
        for item in txtlists:
            if not y == item[1]:
                y = item[1]
                n = '\n'
            else:
                n = ''
            result += n
            result += item[0].encode('utf-8').decode('unicode_escape', 'ignore')
    return result


def parse_txt(doc_id):
    content_url = 'https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id=' + doc_id
    content = fetch_url(content_url)
    md5 = re.findall('"md5sum":"(.*?)"', content)[0]
    pn = re.findall('"totalPageNum":"(.*?)"', content)[0]
    rsign = re.findall('"rsign":"(.*?)"', content)[0]
    content_url = 'https://wkretype.bdimg.com/retype/text/' + doc_id + '?rn=' + pn + '&type=txt' + md5 + '&rsign=' + rsign
    content = json.loads(fetch_url(content_url))
    result = ''
    for item in content:
        for i in item['parags']:
            result += i['c'].replace('\\r', '\r').replace('\\n', '\n')
    return result


def parse_other(doc_id):
    content_url = "https://wenku.baidu.com/browse/getbcsurl?doc_id=" + doc_id + "&pn=1&rn=99999&type=ppt"
    content = fetch_url(content_url)
    url_list = re.findall('{"zoom":"(.*?)","page"', content)
    url_list = [item.replace("\\", '') for item in url_list]
    if not os.path.exists(doc_id):
        os.mkdir(doc_id)
    for index, url in enumerate(url_list):
        content = session.get(url).content
        path = os.path.join(doc_id, str(index) + '.jpg')
        with open(path, 'wb') as f:
            f.write(content)
    print("图片保存在" + doc_id + "文件夹")


def save_file(filename, content):
    with open(filename, 'w', encoding='utf8') as f:
        f.write(content)
        print('已保存为:' + filename)

def get_content_type(content):
    print(re.findall(r"docType.*?\:.*?\'(.*?)\'\,", content))

def get_content_doc(content):
    result = ''
    url_list = re.findall('(https.*?0.json.*?)\\\\x22}', content)
    # print(url_list)
    url_list = [addr.replace("\\\\\\/", "/") for addr in url_list]
    for url in url_list[:-5]:
        content = fetch_url(url)
        y = 0
        txtlists = re.findall('"c":"(.*?)".*?"y":(.*?),', content)
        for item in txtlists:
            if not y == item[1]:
                y = item[1]
                n = '\n'
            else:
                n = ''
            result += n
            result += item[0].encode('utf-8').decode('unicode_escape', 'ignore')
    return result

def main():
    # url = requests.get("https://wenku.baidu.com/view/b12ff5a18462caaedd3383c4bb4cf7ec4afeb69e?fr=sogou&_wkts_=1668521533825").url
    response = requests.get("https://wenku.baidu.com/view/b12ff5a18462caaedd3383c4bb4cf7ec4afeb69e?fr=sogou&_wkts_=1668521533825")
    cookie_value = ''
    for key, value in response.cookies.items():
        cookie_value += key + '=' + value + ';'
    print(str(cookie_value))

    # print("content = "+str(get_content_doc(content)))
if __name__ == "__main__":
    main()