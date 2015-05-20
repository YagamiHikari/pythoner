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
    for i in range(0,len(data)):
        strTxt=strTxt+('%3s\t')%data[i]
        if (i+1)%7==0:
            strTxt=strTxt+'<td>';
    fw.write(strTxt)
    fw.close()

def txtToExcel(text,excel,sheet):
    data=open(text).read()
    lines=data.split('<td>')
    wb=xlwt.Workbook()
    ws=wb.add_sheet(sheet)
    dataStr=''
    for i in range(0,len(lines)):
        fields=lines[i].split('\t')
        for j in range(0,len(fields)):
            ws.write(i,j,fields[j].decode('UTF-8').strip())
    wb.save(excel)
    
def MemberData(path):
    rex='>([^<]*)</td>'
    for fname in os.listdir(path):
        data=open(path+'\\'+fname,'r').read()
        dataResult=re.findall(rex,data)
        dataResult=dataResult[13:len(dataResult)-3]
        saveTxt('money02.txt',dataResult)
        
    txtToExcel('money02.txt','money02.xls','data')
  
if __name__=='__main__':    
    startTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    print 'Begin:'+startTime
    MemberData(r'E:\Python\MayTask\taskData\money')
    EndTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    print '\nEnd:'+EndTime
