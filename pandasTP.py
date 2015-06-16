# -*- coding:UTF-8 -*-
import os,time
from lxml.html import parse
from pandas.io.parsers import TextParser as TP

class dataProcessor:
    # 初始化
    '''path:文件路径；
       name:文件名称
       table:需要提取的表格
       flag:表格的序号
    '''
    def __init__(self,path=None,name=None,\
                 table=None,flag=0):
        self.path=path
        self.name=name
        self.table=table
        self.flag=flag

    # 获得HTML格式的table,并返回给属性table
    def getTable(self):
        parsed=parse(open(self.path))
        doc=parsed.getroot()
        tables=doc.findall('.//table')
        self.table=tables[self.flag]

    # 对table的一行做处理
    def getTr(self,row,kind='td'):
        elts=row.findall('.//%s'%kind)
        return [val.text_content().strip() for val in elts[1:]]

    # 获得格式化的table数据
    def getData(self):
        self.getTable()
        rows=self.table.findall('.//tr')
        # header=self.getTr(rows[0],kind='th')
        data=[self.getTr(r) for r in rows[1:]]
        return TP(data).get_chunk()

    # 保存数据
    def saveTxt(self,data,fname):
        data.to_csv(fname,sep='\t',encoding='utf8'\
                    ,index=False,mode='a')

if __name__=='__main__':
    startTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    tb=dataProcessor()
    tb.path=r'C:\temp\100.html'
    tb.flag=1
    data=tb.getData()
    tb.saveTxt(data,'moneny.txt')
