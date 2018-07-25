from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import *

#basic method: findAll
#findAll(tag,attributes,recursive,text,limit,keywords)
#find等价于findAll中limit等于1时的情景
#eg: .findAll({"h1","h2"})
#eg: .findAll("span",{"class":{"green","blue"}})
#eg: .findAll(id="text")等价于 .findAll("",{"id":"text"})
def basic(url):
    html=urlopen(url)
    obj=BeautifulSoup(html.read())
    nameList=obj.findAll("span",{"class":"green"})
    for name in nameList:
        print(name.get_text())

def tree(url):
    html=urlopen(url)
    obj=BeautifulSoup(html.read())
    #处理子标签以及后代标签
    #一般情况下，BeautifulSoup函数总是会处理当前标签的后代标签，例如，obj.body.h1选择了body标签的后代里的第一个h1标签，不会去找body意外的标签
    print("观察所有标签下面的子标签,用children函数：")
    for child in obj.find("table",{"id":"giftList"}).children:
        print(child)
    print("观察所有标签下面的子标签,用descendants函数：")
    for child in obj.find("table",{"id":"giftList"}).descendants:
        print(child)
    #处理兄弟标签 next_siblings
    #兄弟标签会跳过第一行，因为是用第一行作为起点，遍寻其之后的所有兄弟
    print("观察兄弟标签，用next_siblings")
    for sibling in obj.find("table",{"id":"giftList"}).tr.next_siblings:
        print(sibling)
    #处理父标签parent
    print("观察父标签*******")
    print(obj.find("img",{"src":"../img/gifts/img3.jpg"}).parent.previous_sibling.get_text())

# url="http://www.pythonscraping.com/pages/warandpeace.html"
# basic(url)
url="http://www.pythonscraping.com/pages/page3.html"
tree(url)

