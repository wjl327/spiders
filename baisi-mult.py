#encoding:utf-8
#爬虫百思不得姐的段子，多线程版本，换页的时候不会停顿
import re
import urllib2
import time
import thread

page = 1
pages = []

#格式化文本
def format(content):
        content = re.sub(r'\n', '', content)
        content = re.sub(r'(<p>|</p>)', '', content)
        content = re.sub(r'(<br>|<br/>)', '', content)
        return content

#监听提前缓存两页
def monitor():
        global page,pages
        while True:
            if len(pages) < 2 :
                getPage()
                page+=1
            else:
                time.sleep(5);

#获取指定页面的html
def getPage():
        global page,pages
        qburl = "http://www.budejie.com/duanzi/" + str(page)
        #print '爬第' + str(page) + '页'
        headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36')
        opener = urllib2.build_opener()
        opener.addheaders = [headers]
        ret = opener.open(qburl)
        pg = ret.read().decode("utf-8")
        pages.append(pg)

#正则将html页面的段子匹配出来       
def getContents():
        global pages
        pg = pages[0]
        del pages[0]
        contents = re.findall('<p class="web_size" id=".*?" style="WORD-BREAK: break-all;">(.*?)</div>', pg, re.S)
        return contents

#循环输出格式化之后的每个段子
def printBs():
        global pages
        while len(pages) == 0:
                pass
        while True:
                contents = getContents()
                for content in contents:
                        print format(content).strip(),'[回车查看下一条]'.decode("utf-8")
                        raw_input()


print '阅读启动，如果段子来得慢，可能是网速问题，给点耐心噢~'.decode("utf-8")
print ''

#启动爬虫线程
thread.start_new_thread(monitor,())
printBs()

