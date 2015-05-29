# -*- coding: utf-8 -*-
#模拟登陆武汉大学研究生管理系统
import urllib2,cookielib
import urllib,string
import cStringIO,re
from PIL import Image
import requests

s=requests.Session()      
#获取验证码
s.get('http://gsinfo.whu.edu.cn')  #主页
imgurl = 'http://gsinfo.whu.edu.cn/servlet/GenImg' #验证码
userid = raw_input("StuNO:")
pwd = raw_input("pwd:")
#res = opener.open(urllib2.Request(imgurl))
res=s.get(imgurl)
tempIm = cStringIO.StringIO(res.content)
im = Image.open(tempIm)
im.show()
yzm = raw_input("check:")

postdata = {
    'who':'student',
    'id':userid,
    'pwd':pwd,
    'yzm':yzm
    }
req = s.post(
    url = 'http://gsinfo.whu.edu.cn/servlet/Login_use',
    data = postdata
    )
#已经成功进入系统
#查询成绩
postscore ={
    'queryType':'1',
    'sYear':'-1',
    'function':'queryScoreStu',
    'Submit':'%C8%B7+%B6%A8',
    #or 'Submit':r'确定',
    'flag':'unnull' 
    }
req=s.post(
    url = 'http://gsinfo.whu.edu.cn/score/Svlt_QueryScore', #成绩
    data = postscore
    )  
info=req.content
#打印成绩
pattern = r'<TD width="90" height="25" align="center" valign="middle">([^>]*?)</TD>[\s\S]*?height="25">([^>]*?)</TD>[\s\S]*?25[\s\S]*?25[\s\S]*?25[\s\S]*?25[\s\S]*?25[\s\S]*?25">[\s\S]*?25">([^>]*?)</TD>'
p = re.compile(pattern)
score = p.findall(info)
for i in range(len(score)):
    print score[i][1],score[i][0],string.strip(score[i][2])

