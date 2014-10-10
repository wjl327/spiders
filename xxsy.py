#encoding:utf-8
#爬潇湘书院的月票榜,爬json的情况
import re
import json
import urllib2

qburl = "http://www.xxsy.net/search.aspx?q=&sort=7&rn=15&pn=1&rand=1406000763717" 
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36')
opener = urllib2.build_opener()
opener.addheaders = [headers]
ret = opener.open(qburl) 
unipage = ret.read().decode("utf-8")

try:
    page = json.loads(unipage)
    for bl in page['booklist']:
        print bl['bookname']
         
    
except (ValueError, KeyError, TypeError):
    print "JSON format error"

