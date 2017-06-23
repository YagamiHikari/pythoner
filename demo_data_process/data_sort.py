#! /usr/bin/env python
# coding:utf-8


import time
import operator


def save_txt(text, content):
    """
    save text
    :param text:
    :param content:
    :return:
    """

    fw = open(text, 'a')
    str_txt = ''
    for i, dr in enumerate(content):
        for j, dt in enumerate(dr):
            str_txt = str_txt + '%3s\t' % dt.encode('utf8')
        str_txt = str_txt + '\n'

    fw.write(str_txt)
    fw.close()


def data_sort(text, sort_args):
    """
    data sort
    :param text:
    :param sort_args:
    :return:
    """

    content = open(text, 'r').read()
    lines = content.split('\n')

    data_str = []
    for i, line in enumerate(lines):
        dr = line.split('\t')
        tmp = []
        for j, dd in enumerate(dr):
            tmp.append(dr[j].decode('UTF-8').strip())
        data_str.append(tmp)

    data_str.sort(key=operator.itemgetter(sort_args))
    return data_str


if __name__ == '__main__':

    start_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    print 'Begin:'+start_time

    print 'running...'
    data = data_sort(r'F:\PythonProgram\test.txt', 0)
    save_txt('result.txt', data)

    end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print 'End:'+end_time
