#访寻维基百科链接
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import re
import random


#导入所需要的Python库之后，程序首先做的是用系统当前时间生成一个随机数生成器
#这样，可以保证在每一次程序运行的时候，维基百科词条的选择都是一个全新的随机路径
random.seed(datetime.datetime.now())

#getLink:可以用维基百科词条的形式的URL链接作为参数进行传递，然后以
#同样的形式返回一个列表，里面包含所有的词条URL链接
def getLink(url):
    html=urlopen("https://en.wikipedia.org"+url)
    obj=BeautifulSoup(html.read())
    return obj.find("div",{"id":"bodyContent"}).findAll("a",{"href":re.compile("/wiki/((?!:).)*$")})

#主函数：以某一个其实词条为参数调用getLink，再从返回的URL列表中随机选择一个词条进行链接
#再调用getLink，直到主动停止，或者再新的页面上没有词条链接，程序才停止
links=getLink("/wiki/Kevin_Bacon")
while len(links)>0:
    newArticle=links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links=getLink(newArticle)

#如果要是考虑到去重的问题，可以在函数外围设置set，如果碰到新的元素放入集合，否则pass
#同样考虑的问题还有递归的深度，python默认的递归是1000次，需要设置一个较大的递归计数器