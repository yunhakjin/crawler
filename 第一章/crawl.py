#encoding utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup

def basic():
    html=urlopen("http://www.pythonscraping.com/pages/page1.html")
    obj=BeautifulSoup(html.read())
    print(obj.h1)

basic()
