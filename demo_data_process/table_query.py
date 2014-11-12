#! /usr/bin/env python
# coding:utf-8


import sys
import xlwt
from pyquery import PyQuery as pq

# 解决字符编码转换问题
reload(sys)
sys.setdefaultencoding('utf8')

path = r'content.html'
dates = []
a = open(path, 'r')
book = xlwt.Workbook()
sheet = book.add_sheet('data', cell_overwrite_ok=True)

p = pq(a.read())
number = 0
for data in p('tr'):
    if len(data) > 10:
        for i in range(len(data)):
            item = pq(data).find('td').eq(i).text()or pq(data).find('th').eq(i).text()
            sheet.write(number, i, item.decode('utf-8'))
        number = number + 1
book.save('test.xls')
