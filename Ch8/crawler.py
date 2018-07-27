from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator

def cleanInput(input):
    input=re.sub('\n+'," ",input).lower()
    input=re.sub("\[[0-9]*\]"," ",input)
    input=re.sub(" +"," ",input)
    input=bytes(input,"utf-8")
    input=input.decode("ascii","ignore")
    cleanInput=[]
    input=input.split(" ")
    for item in input:
        item=item.strip(string.punctuation)
        if len(item)>1 or (item.lower()=='a' or item.lower()=='i'):
            cleanInput.append(item)
    return cleanInput

def ngrams(input,n):
    input=cleanInput(input)
    output={}
    for i in range(len(input)-n+1):
        ngramsTemp=" ".join(input[i:i+n])
        if ngramsTemp not in output:
            output[ngramsTemp]=0
        output[ngramsTemp]+=1
    return output

html=urlopen("https://edition.cnn.com/2018/07/26/politics/michael-cohen-donald-trump-russia-meeting/index.html")
obj=BeautifulSoup(html.read())
content=obj.find("section",{"id":"body-text"}).get_text()
# print(content)
ngrams=ngrams(content,2)
sortedNGrams=sorted(ngrams.items(),key=operator.itemgetter(1),reverse=True)
print(sortedNGrams)