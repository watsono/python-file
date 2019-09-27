#!/usr/bin/env python3
# -*- coding = utf-8 -*-
import requests
import re

novel = input("please input the novel's name:")    #输入需要下载的小说名字

search_url = "http://www.mianfeixiaoshuoyueduwang.com/index.php?c=book&a=search&keywords="+novel  #生成搜索URL
response = requests.get(search_url)
requests.coding = "utf-8"
search = response.text

search_name = re.findall(r'cc0000;">(.*?)</b>(.*?)</span>',search)  #清洗数据（小说名）
search_info_url = re.findall(r'<h3><a href="(.*?)" itemprop="url"',search)  #清洗数据（小说链接）
i = 0
x = 0
for name in search_name:
    na1 = name[0]
    na2 = name[1]
    name0 = na1+na2            #获取搜索到的所有结果
    i += 1
    print("%d：%s" % (i,name0))
    print("%d：%s" % (i, search_info_url[i-1]))

n = int(input("please input the number:"))
novel_url = search_info_url[n-1]     #获取目标小说URL

xiaoshuo = requests.get(novel_url)
xiaoshuo.coding = "utf-8"
xiaoshuo = xiaoshuo.text

main_url = re.findall(r'<a href="(.*?)" class="button bc1">查看目录</a>',xiaoshuo)[0]
main_url = 'http://www.qb5.io'+main_url

mulu = requests.get(main_url)
mulu.coding = "utf-8"       #目标小说的界面
mulu = mulu.text

novel_chapter = re.findall(r'<li><a href="(.*?)">(.*?)</a></li>',mulu)  #正则分布

for novel_info_chapter in novel_chapter:
    novel_chapter_url = novel_info_chapter[0]
    novel_chapter_name = novel_info_chapter[1]
    novel_chapter_url = "http://www.qb5.io"+novel_chapter_url

    novel_text = requests.get(novel_chapter_url)
    novel_text.coding = "utf-8"
    novel_text = novel_text.text
    novel_text = re.findall(r'<p>.*?</p>',novel_text)
    novel_text_main = ''
    for novel_info_text in novel_text:
        novel_text_main = novel_text_main+novel_info_text
    novel_text_main = novel_text_main.replace('<p>','  ') #替换<p>和</p>
    novel_text_main = novel_text_main.replace('</p>','\n')
    novel_text_main = novel_text_main.encode('utf-8')
    with open('%s.txt' % novel_chapter_name,'wb') as f:   #保存文件
        f.write(novel_text_main)
    print(novel_chapter_name)