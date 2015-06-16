# -*- coding: utf-8 -*-
#模拟登陆武汉大学研究生管理系统
import string,cStringIO,re
from PIL import Image
import requests,os
import sys,xlrd,xlwt
from pyquery import PyQuery as pq

def login():
    HomeUrl= r'http://gsinfo.whu.edu.cn'
    imgurl = r'http://gsinfo.whu.edu.cn/servlet/GenImg'
    loginUrl= r'http://gsinfo.whu.edu.cn/servlet/Login_use'
    ScoreUrl = r'http://gsinfo.whu.edu.cn/score/Svlt_QueryScore'
    s=requests.session()
    s.get(HomeUrl)
    userid =raw_input("stuNo:")
    pwd =raw_input("pwd:")
    res = s.get(imgurl)
    tempIm = cStringIO.StringIO(res.content)
    im = Image.open(tempIm)
    im.show()
    yzm = raw_input("check:")
    #需要post的数据
    postdata = {
        'who':'student',
        'id':userid,
        'pwd':pwd,
        'yzm':yzm
        }
    s.post(
        url = loginUrl,
        data = postdata
        )

    #已经成功进入系统
    #查询成绩
    postscore ={
        'queryType':'1',
        'sYear':'-1',
        'function':'queryScoreStu',
        'Submit':r'确定',
        'flag':'unnull'}

    r=s.post(
        url = ScoreUrl,
        data = postscore
        )
    return r.content

def scorePrint(content):
    pattern = r'<TD width="90" height="25" align="center" valign="middle">([^>]*?)</TD>[\s\S]*?height="25">([^>]*?)</TD>[\s\S]*?25[\s\S]*?25[\s\S]*?25[\s\S]*?25[\s\S]*?25[\s\S]*?25">[\s\S]*?25">([^>]*?)</TD>'
    p = re.compile(pattern)
    score = p.findall(content)
    for i in range(len(score)):
        print score[i][1],score[i][0],string.strip(score[i][2])

def scoreSave(content):
    #解决字符编码转换问题
    reload(sys)
    sys.setdefaultencoding('utf8')

    book = xlwt.Workbook()
    sheet = book.add_sheet('data',cell_overwrite_ok=True)

    p = pq(content)
    number=0
    for data in p('TR'):
          if len(data)>2:
              for i in range(len(data)):
                  xxx=pq(data).find('TD').eq(i).text()or pq(data).find('TH').eq(i).text()
                  sheet.write(number,i, xxx.decode('utf-8'))
              number=number+1
    book.save('test.xls')

if __name__ == '__main__':
   info=login()
   #fw=open('test.html','a')
   #fw.write(info)
   #fw.close()
   scorePrint(info)
   scoreSave(info)
