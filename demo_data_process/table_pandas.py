#! /usr/bin/env python
# coding:utf-8


from lxml.html import parse
from pandas.io.parsers import TextParser


class DataProcessor:
    """
    Pandas提取html中的table
    """
    def __init__(self, path=None, name=None, table=None, flag=0):
        """

        :param path:
        :param name:
        :param table:
        :param flag: 表格的序号
        """
        self.path = path
        self.name = name
        self.table = table
        self.flag = flag

    def get_table(self):
        """
        获得HTML格式的table,并返回给属性table
        :return:
        """
        parsed = parse(open(self.path))
        doc = parsed.getroot()
        tables = doc.findall('.//table')
        self.table = tables[self.flag]

    @staticmethod
    def get_row(row, kind='td'):
        """

        :param row:
        :param kind:
        :return:
        """
        elts = row.findall('.//%s' % kind)
        return [val.text_content().strip() for val in elts[1:]]

    def get_table_data(self):
        """

        :return:
        """
        self.get_table()
        rows = self.table.findall('.//tr')
        # headers = self.get_row(rows[0], kind='th')
        data = [self.get_row(r) for r in rows[1:]]
        return TextParser(data).get_chunk()

    @staticmethod
    def save_txt(data, filename):
        """

        :param data:
        :param filename:
        :return:
        """
        data.to_csv(filename, sep='\t', encoding='utf8', index=False, mode='a')


if __name__ == '__main__':

    tb = DataProcessor()
    tb.path = r'C:\temp\100.html'
    tb.flag = 1
    content = tb.get_table_data()
    tb.save_txt(content, 'money.txt')
