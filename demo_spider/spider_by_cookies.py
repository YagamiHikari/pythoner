#! /usr/bin/env python
# coding:utf-8


import requests
import time


def login():

    rs = requests.session()
    header = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
            'Host': "www.jkscglobal.com",
            'Referer': "http://www.jkscglobal.com/Stockist/List/Query?status=0&start=2013-2-1&end=2015-09-09&type=1&query=",
            'Cookie': "ASP.NET_SessionId=o5t5ck0niyfyw4jz5zc0uhyv; VCode=JPWNMkSkWaY=; AdminId=1; AdminName=%e8%b6%85%e7%ba%a7%e7%ae%a1%e7%90%86%e5%91%98; LoginName=admin",
            'Connection': "keep-alive",
            'Accept-Language': "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            'Accept-Encoding': "gzip, deflate",
            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    cookies = {
        "ASP.NET_SessionId": "o5t5ck0niyfyw4jz5zc0uhyv",
        "VCode": "JPWNMkSkWaY=",
        "AdminId": "1",
        "AdminName": "%e8%b6%85%e7%ba%a7%e7%ae%a1%e7%90%86%e5%91%98",
        "LoginName": "admin"
    }

    data_page = 'http://www.jkscglobal.com/Stockist/List/Query?page='

    for i in range(1, 50000):

        data_url = data_page + str(i)
        content = rs.get(data_url, headers=header, cookies=cookies).content
        # save(content, 'DsitributionData.txt')
        print 'The '+str(i)+' page finished!'

if __name__ == '__main__':

    startTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print 'Beginning ! Begin:' + startTime

    login()

    EndTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print 'Begin:' + startTime + '\nEnd:' + EndTime

