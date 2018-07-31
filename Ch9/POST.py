import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

#表单提交--文本框
#http://pythonscraping.com/pages/files/processing.php
params={"firstname":"yin","lastname":"xuezhen"}
r=requests.post("http://pythonscraping.com/pages/files/processing.php",data=params)
#print(r.text)

#http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi
params={"email_add":'yxz@163.com'}
r=requests.post("http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi",data=params)
#print(r.text)

#cookie：
#1.http://pythonscraping.com/pages/cookies/login.html
#2.http://pythonscraping.com/pages/cookies/welcome.php
#3.http://pythonscraping.com/pages/cookies/profile.php
#大多数新式的网站都用cookie跟踪用户是否已登录的状态信息。一旦汪涵验证了登录权证，它就会将他们保存在你的浏览器的cookie
#中，里面通常包含一个服务器生成的令牌，登录有效时限和状态跟踪信息。网站会把这个cookie当作信息验证的证据，在你浏览网站的每个
#页面时出示给服务器。但是cookie有时效，所以有可能在某一个时间段后，就要重新提交表单
#在Requests库中session和cookie函数追踪cookie
params={'username':'yxz','password':'password'}
r=requests.post("http://pythonscraping.com/pages/cookies/welcome.php",data=params)
print("Cookie is set to:")
print(r.cookies.get_dict())
print("----------")
print("Going to profile page ..")
r=requests.get("http://pythonscraping.com/pages/cookies/profile.php",cookies=r.cookies)
print(r.text)
print("******************************************************")
session=requests.Session()
s=session.post("http://pythonscraping.com/pages/cookies/welcome.php",params)
print("Cookie is set to:")
print(s.cookies.get_dict())
print("Going to profile page..")
s=session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(s.text)
print('******************************************************')
auth=HTTPBasicAuth('yxz','password')
r=requests.post("http://pythonscraping.com/pages/auth/login.php",auth=auth)
print(r.text)