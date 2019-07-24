from urllib.request import urlopen
from urllib.error import HTTPError
from Yurllib import urllibOpen, urllibDecoding, decodeEnum

def mainUlrOpen(url):
    """
    连接豆瓣阅读提供方列表页面
    :param url:豆瓣阅读提供方列表URL
    """
    # 打开网页
    html = urllibOpen(url)
    if html:
        # 解码
        bsObj = urllibDecoding(html, decodeEnum.UTF8)
        print(bsObj)

if __name__ == "__main__":
    """
    默认启动路径：豆瓣阅读提供方列表页面
    """
    url = "https://read.douban.com/provider/all"
    mainUlrOpen(url)