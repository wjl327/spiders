#encoding:utf-8
#爬17k的榜单
import re
import urllib2

qburl = "http://top.17k.com/phblianzaiclick_wz_week.shtml" 
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36')
opener = urllib2.build_opener()
opener.addheaders = [headers]
ret = opener.open(qburl) 
unipage = ret.read().decode("utf-8")

contents = re.findall('<li.*?class="table_td">(.*?)</li>',unipage, re.S)
for content in contents:
	n = re.findall('<div.*?class="n">(.*?)</div>', content)[0]

	lb = re.findall('<div.*?class="lb">(.*?)</div>', content)[0]
	lb = re.findall('<a.*?href=".*?".*?>(.*?)</a>', lb)[0]


	zp = re.findall('<div.*?class="zp">(.*?)</div>', content)[0]
	zp = re.findall('<a.*?target="_blank".*?title=".*?".*?href=".*?">(.*?)</a>', zp)[0]

	zz = re.findall('<div.*?class="zz">(.*?)</div>', content)[0]
	zz = re.findall('<a.*?target="_blank".*?href=".*?">(.*?)</a>', zz)[0]
	print n,lb,zp,zz

