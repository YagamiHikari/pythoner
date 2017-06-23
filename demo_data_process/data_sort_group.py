#! /usr/bin/env python
# coding:utf-8

import xlwt
from xlrd import open_workbook
from xlutils.copy import copy
import operator
from collections import Counter
from itertools import groupby
from operator import itemgetter


def open_excel(filename):
    """

    :param filename:
    :return:
    """
    try:
        excel = open_workbook(filename)
        return excel
    except Exception as ex:
        print ex
        return False


def sort(excel, data, args):
    """

    :param excel:
    :param data:
    :param args:
    :return:
    """
    data.sort(key=operator.itemgetter(args))
    for dt in data:
        save_excel(excel, dt, len(dt), 'sort')


def sort_sum(data, key=itemgetter(0), field=itemgetter(1)):
    """

    :param data:
    :param key:
    :param field:
    :return:
    """
    for k, gr in groupby(data, key):
        yield k, sum(field(row) for row in gr)


def group(excel, col):
    """

    :param excel:
    :param col:
    :return:
    """

    xls_file = open_workbook(excel)
    sheet = xls_file.sheet_by_index(0)
    tmp = []
    for row in range(0, sheet.nrows):
        if sheet.cell(row, col).value:
            tmp.append(sheet.cell(row, col).value.encode('gb2312'))

    gr = Counter(tmp).most_common()
    str1 = ''
    for i, dt in enumerate(gr):
        dt = gr[i]
        for dd in dt:
            str1 = str1+str(dd)+'\t'
        str1 += '\n'
    print str1

    
def display(excel, sheet):
    """

    :param excel:
    :param sheet:
    :return:
    """

    xls_file = open_workbook(excel)
    try:
        sheet = xls_file.sheet_by_name(sheet)
    except:
        print 'No sheet in %s named.' % sheet
        return

    str1 = ''
    for row in range(0, sheet.nrows):
        for col in range(0, sheet.ncols):
            if sheet.cell(row,col).value:
                str1 += str(sheet.cell(row, col).value.encode('gb2312'))+'\t'
        str1 += '\n'
    print str1


def read(excel, sheet):
    xls_file = open_workbook(excel)
    try:
        sheet = xls_file.sheet_by_name(sheet)
    except:
        print 'No sheet in %s named.' % sheet
        return

    temp = []
    for row in range(0, sheet.nrows):
        row_data = sheet.row_values(row)
        temp.append(row_data)
    return temp


def save_excel(excel, data, col, sheet):
    """

    :param excel:
    :param data:
    :param col:
    :param sheet:
    :return:
    """

    excel_data = open_excel(excel)
    if not excel_data:
        wb = xlwt.Workbook()
        ws = wb.add_sheet(sheet)
        for i in range(0, col):
            ws.write(0, i, data[i])
    else:
        wb = copy(excel_data)
        ws = wb.get_sheet(0)
        table = excel_data.sheets()[0]
        row = table.nrows
        for i in range(0, col):
            ws.write(row, i, data[i])

    wb.save(excel)


if __name__ == '__main__':

    group(r'test.xls', 3, 'testdata.txt')
    content = read(r'data.xls', 'data')
    sort(r'test_sort.xls', content, 1)
    group(r'test_group.xls', content, 1)

    for r, total in sort_sum(sorted(content)):
        print '%1s:%d' % (r, total)
