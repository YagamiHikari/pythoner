#coding:utf-8
import urllib
import time
url=['']*500
page=1
link=1
while page<10:
    #捕获某页
    print '第'+str(page)+'页：'
    con=urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_'+str(page)+'.html').read()
    i=0
    title=con.find(r'<a title=')
    href=con.find(r'href=',title)
    html=con.find(r'.html',href)
    while title!=-1 and href!=-1 and html!=-1 and i<50:
        url[i]=con[href+6:html+5]
        print '第'+str(link)+'篇：'+url[i]
        title=con.find(r'<a title=',html)
        href=con.find(r'href=',title)
        html=con.find(r'.html',href)
        i=i+1
        link=link+1
    else:
        print 'find end!'
    page=page+1
else:
    print 'All pages find end!'


    
j=0
while j<50:
    content=urllib.urlopen(url[j]).read()
    open(r'HBlog/'+url[j][-26:],'w+').write(content)
    print 'Downloading ',url[j]
    j=j+1
    time.sleep(15)
else:
    print 'Download artilce finished!'
