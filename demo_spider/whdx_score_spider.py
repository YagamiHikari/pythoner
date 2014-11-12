#! /usr/bin/env python
# coding:utf-8

"""
模拟登陆武汉大学研究生管理系统
"""


import string
import cStringIO
import re
from PIL import Image
import requests
import sys
import xlwt
from pyquery import PyQuery as pq

# 解决字符编码转换问题
reload(sys)
sys.setdefaultencoding('utf8')


def login():
    """
    模拟登陆武汉大学研究生管理系统
    :return:
    """

    home_url = r'http://gsinfo.whu.edu.cn'
    img_url = r'http://gsinfo.whu.edu.cn/servlet/GenImg'
    login_url = r'http://gsinfo.whu.edu.cn/servlet/Login_use'
    score_url = r'http://gsinfo.whu.edu.cn/score/Svlt_QueryScore'

    rs = requests.session()
    rs.get(home_url)
    userid = raw_input("stuNo:")
    pwd = raw_input("pwd:")
    res = rs.get(img_url)
    temp_img = cStringIO.StringIO(res.content)
    im = Image.open(temp_img)
    im.show()

    yzm = raw_input("check:")
    postdata = {
        'who': 'student',
        'id': userid,
        'pwd': pwd,
        'yzm': yzm
    }
    rs.post(url=login_url, data=postdata)

    # 已经成功进入系统
    # 查询成绩
    postscore = {
        'queryType': '1',
        'sYear': '-1',
        'function': 'queryScoreStu',
        'Submit': r'确定',
        'flag': 'unnull'
    }

    response = rs.post(url=score_url, data=postscore)
    return response.content


def print_score(content):
    """

    :param content:
    :return:
    """

    pattern = r'<TD width="90" height="25" align="center" valign="middle">' \
              r'([^>]*?)</TD>[\s\S]*?height="25">([^>]*?)</TD>' \
              r'[\s\S]*?25[\s\S]*?25[\s\S]*?25[\s\S]*?25[\s\S]*?25[\s\S]*?25">' \
              r'[\s\S]*?25">([^>]*?)</TD>'
    rex = re.compile(pattern)
    score = rex.findall(content)
    for i in range(len(score)):
        print score[i][1], score[i][0], string.strip(score[i][2])


def save_score(content):
    """

    :param content:
    :return:
    """

    book = xlwt.Workbook()
    sheet = book.add_sheet('data', cell_overwrite_ok=True)

    p = pq(content)
    number = 0
    for data in p('TR'):
        if len(data) > 2:
            for i in range(len(data)):
                item = pq(data).find('TD').eq(i).text()or pq(data).find('TH').eq(i).text()
                sheet.write(number, i, item.decode('utf-8'))
            number = number+1
    book.save('score.xls')


if __name__ == '__main__':

    info = login()
    print_score(info)
    save_score(info)
