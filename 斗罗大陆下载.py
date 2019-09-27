#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
import re
url = 'https://www.sangwu.org/book/0/308/'
response = requests.get(url)
response.encoding = 'gbk'
html = response.text
dl = re.findall(r'<dl>.*?</dl>',html,re.S)[0]
title = re.findall(r'<dt>(.*?)</dt>',dl)[0]
fb = open('%s.txt' % title, 'w', encoding='utf-8')
chapter_info_list = re.findall(r'href="(.*?)">(.*?)<',dl)
for chapter_info in chapter_info_list:
    chapter_url = chapter_info[0]
    chapter_title = chapter_info[1]
    fb.write(chapter_title)
    fb.write('\n')
    chapter_url = "https://www.sangwu.org/book/0/308/%s" % chapter_url
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = 'gbk'
    chapter_html = chapter_response.text
    chapter_content = re.findall(r'\<div class="centent">(.*?)</div>',chapter_html,re.S)[0]
    chapter_content = chapter_content.replace(' ','')
    chapter_content = chapter_content.replace('&nbsp;',' ')
    chapter_content = chapter_content.replace('<br/>','  ')
    fb.write(chapter_content)
    fb.write('\n')
    fb.write('\n')
    fb.write('\n')  
    fb.write('\n')    
    print(chapter_title)
print(title) 