#!/usr/bin/env python3
#  -*- coding=utf-8 -*-
import requests
import re
url = "http://www.youmeitu.com/meinv/"
res = requests.get(url)
res.encoding = 'utf-8'
html = res.text
dl = re.findall(r"<ul>.*?</ul>", html, re.S)
dl = str(dl)

image_info_list = re.findall(r'img src=".*?">.*?</span',dl,re.S)
for image_info in image_info_list:
    image_info_url = re.findall(r'img src="(.*?)"',image_info)
    image_info_title = re.findall(r'<span>(.*?)</span>',image_info)
    image1 = image_info_url[0]
    image2 = image_info_url[1]
    title1 = image_info_title[0]
    fb = open('E:\\image\\%s.jpg' % title1, 'wb')
    fb.write(requests.get(image1).content)
    fb.write(requests.get(image2).content)
    print(title1)