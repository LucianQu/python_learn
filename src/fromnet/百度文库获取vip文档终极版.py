import requests
import requests as _requests
from bs4 import BeautifulSoup as _soup
from docx import Document  # 需要安装第三方库python-docx
from docx.oxml.ns import qn  # 中文格式
from docx.shared import Pt  # 用于设置字体样式

PROGRESS_BAR = '█'

HTTP = 'http'
HTTPS = 'https'
SOCKS = 'socks'

USER_AGENT = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/68.0.3440.106 Safari/537.36'
)

CP936 = CP_936 = 'cp936'
UTF_8 = UTF8 = 'utf-8'
UTF_16 = UTF16 = 'utf-16'
UTF_32 = UTF32 = 'utf-32'
USC_2 = USC2 = 'usc-2'
USC_4 = USC4 = 'usc-4'
UTF_16_BE = UTF16BE = 'uft-16-BE'
UTF_16_LE = UTF16LE = 'uft-16-LE'
ASCII = ANSI = 'ansi'
LATIN_1 = LATIN1 = 'Latin-1'
GBK = 'gbk'
GB2312 = GB_2312 = 'gb2312'
GB18030 = GB_18030 = 'gb18030'
ISO = ISO_8859_1 = 'ISO-8859-1'

HTML_PARSER = DEFAULT_PARSER = 'html.parser'
XML = XML_PARSER = 'xml'
LXML = LXML_PARSER = 'lxml'
LXML_XML = LXML_XML_PARSER = 'lxml-xml'
HTML5LIB = HTML5LIB_PARSER = 'html5lib'


class BaiduLibrary(object):
    def __init__(self, url: str, cookie: str = '', proxy_ip: str = None, proxy_type: str = HTTPS,
                 encoding: str = 'utf-8', parser=HTML_PARSER):
        self.encoding = encoding
        self.url = url
        self.headers = {
            'Cookie': cookie,
            'User-Agent': USER_AGENT
        }
        self.parser = parser
        self._use_proxy_ip = proxy_ip is not None
        self.proxies = {proxy_type: proxy_ip}
        self._request()

    def _request(self):
        if self._use_proxy_ip:
            self.response = _requests.get(self.url, headers=self.headers, proxies=self.proxies)
        else:
            self.response = _requests.get(self.url, headers=self.headers)
        self.response.encoding = self.encoding
        self.soup = _soup(self.response.text, self.parser)
    def get(self):
        # texts = self.soup.find_all('p', attrs={'v-pre': '', 'class': 'reader-word-layer'})
        texts = self.soup.find_all('p', attrs={'v-pre': '', 'class': 'creader-interative-canvas'})
        print(str(texts))
        texts = [i.string for i in texts]
        result = ''.join(texts)
        result = result.replace('\u2002', ' ')
        return result


BaiduWenKu = BaiduLibrary

# 这里cookie换成你自己的



def main():
    url="https://wenku.baidu.com/view/b12ff5a18462caaedd3383c4bb4cf7ec4afeb69e?aggId=b12ff5a18462caaedd3383c4bb4cf7ec4afeb69e&fr=catalogMain&_wkts_=1668739885151"
    # url = requests.get("https://wenku.baidu.com/view/b12ff5a18462caaedd3383c4bb4cf7ec4afeb69e?fr=sogou&_wkts_=1668521533825").url
    response = requests.get(url)
    cookie_value = ''
    for key, value in response.cookies.items():
        cookie_value += key + '=' + value + ';'
    print(cookie_value)
    bl = BaiduLibrary(url, cookie=cookie_value)
    result = bl.get()
    print(result)
    # docx_path = "自评与互评教学反思.docx"
    doc = Document()
    doc.styles["Normal"].font.name = u"宋体"  # 设置字体样式
    doc.styles["Normal"].font.size = Pt(14)  # 设置字体大小
    doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')  # 设置文档的基础样式
    doc.add_paragraph(result)  # 增加一个paragraph,写入内容
    doc.save(r"D:\python\doc\自评与互评教学反思.docx")
    # print("content = "+str(get_content_doc(content)))
if __name__ == "__main__":
    main()