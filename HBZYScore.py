# -*- coding:utf-8 -*-
#模拟登录湖北中医药大学教务管理系统
import urllib,requests
import urllib2,string
import cStringIO,re
from PIL import Image

s=requests.session()
#获取验证码
s.get('http://218.197.176.40/%28trx14ynx5mrpawvrsckaoc45%29/default2.aspx')
imgurl=r'http://218.197.176.40/%28trx14ynx5mrpawvrsckaoc45%29/CheckCode.aspx'

userid=raw_input("stuNo:")
pwd=raw_input("Pwd:")
res=s.get(imgurl)
tempIm=cStringIO.StringIO(res.content)
im=Image.open(tempIm)
im.show()
check=raw_input("check:")

#需要提交的数据
postdata={
    '__VIEWSTATE':'dDwyODE2NTM0OTg7Oz6muYERwaRLIwixbRj0d2MDTfY7oA==',
    'txtUserName':userid,
    'TextBox2':pwd,
    'txtSecretCode':check,
    'RadioButtonList1':r'学生',
    'Button1':'',
    'lbLanguage':'',
    'hidPdrs':'',
    'hidsc':''
    }
loginUrl=r'http://218.197.176.40/%28trx14ynx5mrpawvrsckaoc45%29/default2.aspx'
req=s.post(
    url=loginUrl,
    data=postdata
    )

obj=re.search(r'&xm=([^<]*)&',req.content,re.M|re.I)
if obj:
    username=obj.group(1)
    print '登录成功！'
else:
    print '登录失败，请重新登录！'
    username=''
#print req.content

scoreurl='http://218.197.176.40/(4fxwaj55zvzyciqp31ngcrqq)/xscjcx.aspx?xscjcx.aspx?xh=20090701027&xm=%D5%C5%B2%AE%B3%C9&gnmkdm=N121605'

print scoreurl
scoreData={
    'xh':userid,
    'xm':r'张伯成',#username.decode('gb2312','ignore').encode('utf8'),
    'gnmkdm':'N121605',
    '__EVENTTARGET':'',
    '__VIEWSTATE':'dDwxMjQwNjk5NDEyO3Q8cDxsPFNvcnRFeHByZXM7c2ZkY2JrO2RnMztkeWJ5c2NqO1NvcnREaXJlO3hoO3N0cl90YWJfYmpnO2NqY3hfbHNiO3p4Y2pjeHhzOz47bDxrY21jO1xlO2JqZztcZTthc2M7MjAwOTA3MDEwMjc7emZfY3hjanRqXzIwMDkwNzAxMDI3OzsxOz4+O2w8aTwxPjs+O2w8dDw7bDxpPDQ+O2k8MTA+O2k8MTk+O2k8MjQ+O2k8MzI+O2k8MzQ+O2k8MzY+O2k8Mzg+O2k8NDA+O2k8NDI+O2k8NDQ+O2k8NDY+O2k8NTA+O2k8NTI+Oz47bDx0PHQ8O3Q8aTwxNj47QDxcZTsyMDAxLTIwMDI7MjAwMi0yMDAzOzIwMDMtMjAwNDsyMDA0LTIwMDU7MjAwNS0yMDA2OzIwMDYtMjAwNzsyMDA3LTIwMDg7MjAwOC0yMDA5OzIwMDktMjAxMDsyMDEwLTIwMTE7MjAxMS0yMDEyOzIwMTItMjAxMzsyMDEzLTIwMTQ7MjAxNC0yMDE1OzIwMTUtMjAxNjs+O0A8XGU7MjAwMS0yMDAyOzIwMDItMjAwMzsyMDAzLTIwMDQ7MjAwNC0yMDA1OzIwMDUtMjAwNjsyMDA2LTIwMDc7MjAwNy0yMDA4OzIwMDgtMjAwOTsyMDA5LTIwMTA7MjAxMC0yMDExOzIwMTEtMjAxMjsyMDEyLTIwMTM7MjAxMy0yMDE0OzIwMTQtMjAxNTsyMDE1LTIwMTY7Pj47Pjs7Pjt0PHQ8cDxwPGw8RGF0YVRleHRGaWVsZDtEYXRhVmFsdWVGaWVsZDs+O2w8a2N4em1jO2tjeHpkbTs+Pjs+O3Q8aTw1PjtAPOW/heS/rjvpmZDpgIk75YWs6YCJO+mAmuivhjtcZTs+O0A8MDE7MDI7MDM7MDQ7XGU7Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPFxlOz4+Oz47Oz47dDxwPHA8bDxUZXh0O1Zpc2libGU7PjtsPOWtpuWPt++8mjIwMDkwNzAxMDI3O288dD47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7VmlzaWJsZTs+O2w85aeT5ZCN77ya5byg5Lyv5oiQO288dD47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7VmlzaWJsZTs+O2w85a2m6Zmi77ya5L+h5oGv5oqA5pyv57O7O288dD47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7VmlzaWJsZTs+O2w85LiT5Lia77yaO288dD47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7VmlzaWJsZTs+O2w85L+h5oGv566h55CG5LiO5L+h5oGv57O757ufO288dD47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS4k+S4muaWueWQkTrml6DmlrnlkJE7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7VmlzaWJsZTs+O2w86KGM5pS/54+t77yaMjAwOee6p+S/oeaBr+euoeeQhuS4juS/oeaBr+ezu+e7nztvPHQ+Oz4+Oz47Oz47dDw7bDxpPDE+O2k8Mz47aTw1PjtpPDc+O2k8OT47aTwxMT47aTwxMz47aTwxNT47aTwxNz47aTwxOD47aTwxOT47aTwyMT47aTwyMz47aTwyNT47aTwyNz47aTwyOT47aTwzNT47aTw0MT47aTw0Mz47aTw0ND47PjtsPHQ8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+Pjs+Ozs+O3Q8QDA8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+PjtwPGw8c3R5bGU7PjtsPERJU1BMQVk6bm9uZTs+Pj47Ozs7Ozs7Ozs7Pjs7Pjt0PDtsPGk8MTM+Oz47bDx0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+O3Q8cDxwPGw8VGV4dDtWaXNpYmxlOz47bDzoh7Pku4rmnKrpgJrov4for77nqIvmiJDnu6nvvJo7bzx0Pjs+Pjs+Ozs+O3Q8QDA8cDxwPGw8UGFnZUNvdW50O18hSXRlbUNvdW50O18hRGF0YVNvdXJjZUl0ZW1Db3VudDtEYXRhS2V5czs+O2w8aTwxPjtpPDA+O2k8MD47bDw+Oz4+O3A8bDxzdHlsZTs+O2w8RElTUExBWTpibG9jazs+Pj47Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47cDxsPHN0eWxlOz47bDxESVNQTEFZOm5vbmU7Pj4+Ozs7Ozs7Ozs7Oz47Oz47dDxAMDxwPHA8bDxWaXNpYmxlOz47bDxvPGY+Oz4+O3A8bDxzdHlsZTs+O2w8RElTUExBWTpub25lOz4+Pjs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8Ozs7Ozs7Ozs7Oz47Oz47dDxAMDxwPHA8bDxWaXNpYmxlOz47bDxvPGY+Oz4+O3A8bDxzdHlsZTs+O2w8RElTUExBWTpub25lOz4+Pjs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+PjtwPGw8c3R5bGU7PjtsPERJU1BMQVk6bm9uZTs+Pj47Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+PjtwPGw8c3R5bGU7PjtsPERJU1BMQVk6bm9uZTs+Pj47Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47cDxsPHN0eWxlOz47bDxESVNQTEFZOm5vbmU7Pj4+Ozs7Ozs7Ozs7Oz47Oz47dDxAMDw7QDA8OztAMDxwPGw8SGVhZGVyVGV4dDs+O2w85Yib5paw5YaF5a65Oz4+Ozs7Oz47QDA8cDxsPEhlYWRlclRleHQ7PjtsPOWIm+aWsOWtpuWIhjs+Pjs7Ozs+O0AwPHA8bDxIZWFkZXJUZXh0Oz47bDzliJvmlrDmrKHmlbA7Pj47Ozs7Pjs7Oz47Ozs7Ozs7Ozs+Ozs+O3Q8cDxwPGw8VGV4dDtWaXNpYmxlOz47bDzmnKzkuJPkuJrlhbE0M+S6ujtvPGY+Oz4+Oz47Oz47dDxwPHA8bDxWaXNpYmxlOz47bDxvPGY+Oz4+Oz47Oz47dDxwPHA8bDxWaXNpYmxlOz47bDxvPGY+Oz4+Oz47Oz47dDxwPHA8bDxWaXNpYmxlOz47bDxvPGY+Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDxTQ1VUOz4+Oz47Oz47dDxwPHA8bDxJbWFnZVVybDs+O2w8Oz4+Oz47Oz47Pj47dDw7bDxpPDM+Oz47bDx0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+Oz4+Oz5xBUWUjd78Byv29XN2YDRv0TBKTQ==',
    'hidLanguage':'',
    'ddlXN':'',
    'ddlXQ':'',
    'ddl_kcxz':'',
    'btn_zcj':r'历年成绩'
    }
req=s.post(
    url = scoreurl,
    data = scoreData
    )  
info=req.content
print info
