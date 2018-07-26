from urllib.request import urlopen
from bs4 import BeautifulSoup
import re,string

def cleanInput(input):
    input=re.sub('\n+'," ",input)  #内容中的换行符替换成空格
    input=re.sub(" +"," ",input)   #连续的多个空格替换成一个空格
    input=bytes(input,'UTF-8')     #转换成UTF-8格式以消除转义字符
    input=input.decode("ascii","ignore")
    input=input.split(" ")
    cleanInput=[]
    for item in input:
        item=item.strip(string.punctuation)  #获取python中的所有标点符号，单词两端的任何标点会被去掉
        if len(item)>1 or (item.lower()=='a' or item.lower()=='i'):
            cleanInput.append(item)
    return cleanInput

def ngrams(input,n):
    input=cleanInput(input)
    output=[]
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

html=urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
obj=BeautifulSoup(html.read())
content=obj.find("div",{"id":"mw-content-text"}).get_text()
ngrams=ngrams(content,2)
print(ngrams)

