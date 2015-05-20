# -*- coding: UTF-8 -*-
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy
import operator
from collections import Counter

def open_excel(filename):
    try:
        excel=open_workbook(filename)
        return excel
    except:
        return 0

def Group(excel,col,txt):
    xlsfile=open_workbook(excel)
    sheet=xlsfile.sheet_by_index(0)
    tmp=[]
    for row in range(0,sheet.nrows):
        if sheet.cell(row,col).value!=None:
            tmp.append(sheet.cell(row,col).value.encode('gb2312'))
    gr=Counter(tmp).most_common()
    str1=''
    for i,dt in enumerate(gr):
        dt=gr[i]
        for dd in dt:
            str1=str1+str(dd)+'\t'
        str1+='\n'
    fw=open(txt,'a')
    fw.write(str1)
    fw.close()
    
def display(excel,sheet):
    xlsfile=open_workbook(excel)
    try:
        sheet=xlsfile.sheet_by_name(sheet)
    except:
        print 'No sheet in %s named.'%sheet
        return
    str1=''
    for row in range(0,sheet.nrows):
        for col in range(0,sheet.ncols):
            if sheet.cell(row,col).value!=None:
                str1+=str(sheet.cell(row,col).value.encode('gb2312'))+'\t'
        str1+='\n'
    print str1

def Read(excel,sheet):
    xlsfile=open_workbook(excel)
    try:
        sheet=xlsfile.sheet_by_name(sheet)
    except:
        print 'No sheet in %s named.'%sheet
        return
    temp=[]
    for row in range(0,sheet.nrows):
        row_data=sheet.row_values(row)
        temp.append(row_data)
    return temp

def Sort(excel,data,args):
    data.sort(key=operator.itemgetter(args))
    for dt in data:
        saveExcel(excel,dt,len(dt),'sort')
        
def saveExcel(excel,data,col,sheet):
    excelData=open_excel(excel)
    if excelData==0:
        wb=xlwt.Workbook()
        ws=wb.add_sheet(sheet)
        for i in range(0,col):
            ws.write(0,i,data[i])
    else:
        wb=copy(excelData)
        ws=wb.get_sheet(0)
        table=excelData.sheets()[0]
        row=table.nrows
        for i in range(0,col):
            ws.write(row,i,data[i])
    wb.save(excel)
	
if __name__=='__main__':
    Group(r'test.xls',3,'testdata.txt')
    data=Read(r'test.xls','test_data')
    Sort(r'test_sort.xls',data,1)
   
