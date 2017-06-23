#! /usr/bin/env python
# coding:utf-8


"""
模拟登陆武汉大学研究生管理系统
"""

import urllib2
import cookielib
import urllib
import string
import cStringIO
import re
from PIL import Image


cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
opener.addheaders.append(('User-Agent','Mozilla/5.0 (Windows NT 5.1; rv:25.0) Gecko/20100101 Firefox/25.0'))
opener.addheaders.append(('Connection','Keep-Alive'))

opener.open(urllib2.Request('http://gsinfo.whu.edu.cn'))

img_url = 'http://gsinfo.whu.edu.cn/servlet/GenImg'
user_id = raw_input("学号：")
pwd = raw_input("密码：")
res = opener.open(urllib2.Request(img_url))
tempIm = cStringIO.StringIO(res.read())
im = Image.open(tempIm)
im.show()
yzm = raw_input("验证码：")

postdata = urllib.urlencode({
    'who': 'student',
    'id': user_id,
    'pwd': pwd,
    'yzm': yzm,
    'submit.x': 0,
    'submit.y': 0
})
req = urllib2.Request(url='http://gsinfo.whu.edu.cn/servlet/Login_use', data=postdata)
opener.open(req)

# 已经成功进入系统
# 查询成绩
postscore = urllib.urlencode({
    'queryType': '1',
    'sYear': '-1',
    'function': 'queryScoreStu',
    'Submit': '%C8%B7+%B6%A8',
    'flag': 'unnull'
})
req = urllib2.Request(url='http://gsinfo.whu.edu.cn/score/Svlt_QueryScore', data=postscore)
 
result = opener.open(req)
info = result.read()
# print info

# 打印成绩
pattern = r'<TD width="90" height="25" align="center" valign="middle">([^>]*?)</TD>' \
          r'[\s\S]*?height="25">([^>]*?)</TD>[\s\S]*?25[\s\S]*?25[\s\S]*?25[\s\S]*?25' \
          r'[\s\S]*?25[\s\S]*?25">[\s\S]*?25">([^>]*?)</TD>'
p = re.compile(pattern)
score = p.findall(info)
for i in range(len(score)):
    print score[i][1], score[i][0], string.strip(score[i][2])
