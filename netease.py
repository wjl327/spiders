#coding:utf-8 
#encoding:utf-8
#网易新闻
import re
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

qburl = "http://www.163.com" 
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36')
opener = urllib2.build_opener()
opener.addheaders = [headers]
ret = opener.open(qburl) 
unipage = ret.read()

newsList = re.findall(r'(<a.*?href="(http://news\.163\.com/\d.*?)".*?>(.*?)</a>)', unipage)


contents = []
for news in newsList:
	#python 变态中文乱码 
	contents.append('标题：' + news[2].decode('gb2312', 'ignore').encode('utf-8') + '\n')
	contents.append('链接：' +news[1] + '\n\n')

f = open("163News.txt", "w")
f.writelines(contents)
f.close() 