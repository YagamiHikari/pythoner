# -*- coding:UTF-8 -*-
import os
import os.path
import re
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy
import time
import operator
import codecs

def saveTxt(text,data):
    fw=open(text,'a')
    strTxt=''
    for i,dr in enumerate(data):
        for j,dt in enumerate(dr):
            strTxt=strTxt+('%3s\t')%dt.encode('utf8')
        strTxt=strTxt+'\n';
    fw.write(strTxt)
    fw.close()
    
def dataSort(text,sortArgs):
    data=open(text,'r').read()
    lines=data.split('\n')
    dataStr=[]
    for i,line in enumerate(lines):
        dataRow=line.split('\t')
        tmp=[]
        for j,dd in enumerate(dataRow):
            tmp.append(dataRow[j].decode('UTF-8').strip())
        dataStr.append(tmp)
    dataStr.sort(key=operator.itemgetter(sortArgs))
    return dataStr

if __name__=='__main__':
    startTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    print 'Begin:'+startTime
    print 'running...'
    data=dataSort(r'F:\PythonProgram\test.txt',0)
    saveTxt('Result.txt',data)
    EndTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    print 'End:'+EndTime
