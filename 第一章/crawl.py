#coding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError,URLError

#描述的是最基本的爬虫
def basic():
    html=urlopen("http://www.pythonscraping.com/pages/page1.html")
    obj=BeautifulSoup(html.read())
    print(obj.h1)

"""
描述在考虑传输错误的时候的异常处理：
1.网页在服务器上不存在  404
2.服务器不存在 500
这两个部分体现在第一个except中
1.标签不存在或者获取不到
这部分体现在第二个except中
"""
def deal_exeception():
    try:
        html=urlopen("http://www.pythonscraping.com/pages/page1.html")
    except (HTTPError,URLError) as e:
        return None
    try:
        obj=BeautifulSoup(html.read())
        title=obj.body.h1
    except AttributeError as e:
        return None
    print(title)


basic()
deal_exeception()
