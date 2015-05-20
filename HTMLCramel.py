# -*- coding:UTF-8 -*-
import os
import os.path
import re
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy
import time

def saveTxt(text,data):
    fw=open(text,'a')
    strTxt=""
    for txt in data:
        strTxt=strTxt+('%30s\t')%txt
    fw.write(strTxt+'\n')
    fw.close()

def txtToExcel(text,excel,sheet):
    data=open(text).read()
    lines=data.split('\n')
    wb=xlwt.Workbook()
    ws=wb.add_sheet(sheet)
    dataStr=''
    for i in range(0,len(lines)):
        fields=lines[i].split('\t')
        for j in range(0,len(fields)):
            ws.write(i,j,fields[j].decode('UTF-8').strip())
    wb.save(excel)
    
def MemberData(path):
    rex='>([^<]*)</span></td>'
    for fname in os.listdir(path):
        data=open(path+'\\'+fname,'r').read()
        dataResult=re.findall(rex,data)
        saveTxt('user02.txt',dataResult)
    txtToExcel('user02.txt','user02.xls','data')
    
if __name__=='__main__':
    startTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()) 
    MemberData(r'E:\Python\MayTask\taskData\user')
    EndTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    print 'Begin:'+startTime,'\nEnd:'+EndTime 
