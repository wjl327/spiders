#encoding:utf-8
#爬虫百思不得姐
import re
import urllib2

def format(content):
        content = re.sub(r'\n', '', content)
        content = re.sub(r'(<p>|</p>)', '', content)
        content = re.sub(r'(<br>|<br/>)', '', content)
        return content

def getPage(pg):
        qburl = "http://www.budejie.com/duanzi/" + str(pg)
        headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36')
        opener = urllib2.build_opener()
        opener.addheaders = [headers]
        ret = opener.open(qburl)
        page = ret.read().decode("utf-8")
        return page
                        
def getContents(pg):
        page = getPage(pg)
        contents = re.findall('<p class="web_size" id=".*?" style="WORD-BREAK: break-all;">(.*?)</div>', page, re.S)
        return contents

def printBs(pg):
        contents = getContents(pg)
        for content in contents:
                print format(content).strip(),'[回车查看下一条]'.decode("utf-8")
                raw_input()
        printBs(pg + 1)


print '阅读启动，如果段子来得慢，可能是网速问题，给点耐心噢~'.decode("utf-8")
print ''
printBs(1)