
import re
from urllib import request
def getSortList(sort,page=1):
    res='http://www.quanshuwang.com/list/%s_%s.html' %(sort,page)
    html=request.urlopen(res).read().decode('gbk')
    reg = r'<a target="_blank" title="(.*?)" href="(.*?)" class="clearfix stitle">'
    return re.findall(reg,html)

def getNovelContent(url):
    html=request.urlopen(url).read().decode('gbk')
    reg=r'<a href="(.*?)" class="reader" title=".*?">开始阅读</a>'
    return re.findall(reg,html)

def getChapterContent(url):
    print(url)
    html=request.urlopen(url).read().decode('gbk')
    reg=r'<a href="(.*?)" class="reader" title=".*?免费阅读">开始阅读</a>'
    return re.findall(reg,html)

def getChapterlist(url):
    html=request.urlopen(url).read().decode('gbk')
    reg=r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    return re.findall(reg,html)

def getChapterContent(url):
    html=request.urlopen(url).read().decode('gbk')
    reg = r'<script type="text/javascript">style5\(\);</script>(.*?)<script type="text/javascript">style6();</script></div>'
    reg1=re.compile(reg,re.S)
    return re.findall(reg1,html)


for sort in list(range(1,3)):
    for page in list(range(1,3)):
        for name,url in getSortList(page):
            print(name)
            for novelUrl in getNovelContent(url):
                for chapurl,chapname in getChapterlist(novelUrl):
                    print(chapname)
                    for content in getChapterContent(chapurl):
                        print(content)









