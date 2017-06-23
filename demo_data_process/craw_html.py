#! /usr/bin/env python
# coding:utf-8


import os
import os.path
import re
import xlwt
import time


def save_txt(text, data):
    """

    :param text:
    :param data:
    :return:
    """

    fw = open(text, 'a')
    str_txt = ""
    for i in range(0, len(data)):
        str_txt = str_txt + '%3s\t' % data[i]
        if (i+1) % 7 == 0:
            str_txt = str_txt + '<td>'
    fw.write(str_txt)
    fw.close()


def txt_to_excel(text, excel, sheet):
    """

    :param text:
    :param excel:
    :param sheet:
    :return:
    """

    data = open(text).read()
    lines = data.split('<td>')
    wb = xlwt.Workbook()
    ws = wb.add_sheet(sheet)

    for i in range(0, len(lines)):
        fields = lines[i].split('\t')
        for j in range(0, len(fields)):
            ws.write(i, j, fields[j].decode('UTF-8').strip())
    wb.save(excel)


def get_data(path):
    """

    :param path:
    :return:
    """
    rex = '>([^<]*)</td>'
    for fn in os.listdir(path):
        data = open(path+'\\'+fn, 'r').read()
        data_result = re.findall(rex, data)
        data_result = data_result[13:len(data_result)-3]
        save_txt('money.txt', data_result)
        
    txt_to_excel('money.txt', 'money.xls', 'data')
  
if __name__ == '__main__':

    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print 'Begin:' + start_time
    get_data(r'E:\Python\MayTask\taskData\money')
    end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print '\nEnd:' + end_time
