from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def urllibOpen(url):
    """
    通过urlopen尝试打开网页
    :param url:网页地址
    """
    try:
        # 打开网页
        html = urlopen(url)
    except HTTPError as e:
        # 网页返回异常
        print("HTTPError : " + e)
    else:
        # 网址不存在
        if html is None:
            print("Url Not Found : " + url)
    # 返回获取结果
    return html

def urllibDecoding(html):
    """
    解码网页
    :param html:网页Html内容
    """
    return BeautifulSoup(html.read().decode("utf-8"),"html.parser")