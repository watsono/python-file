#!/usr/bin/env python3
# -*- coding = utf-8 -*-
import requests
import re       # 导入数据库

i = 1
while i <= 1134:
    if i ==1:
        url = "http://pic.netbian.com"
    else:
        url = "http://pic.netbian.com/index_%d.html" % i
    print(url)
    response = requests.get(url)
    response.encoding = "GBK"
    html = response.text

    image_url = re.findall(r'<img src="(.*?)" alt="(.*?)">',html,re.S)
    b = 1
    for image_info_url in image_url:
        image_list_url = image_info_url[0]                                #图片的url
        image_list_name = re.findall(r'(.*?)" />',image_info_url[1])[0]   #图片名字
        image_list_url = "http://pic.netbian.com" + image_list_url        #生成完整的url
        image_response = requests.get(image_list_url)
        image_response.encoding = "utf-8"
        image = image_response.content                                    #生成图片的二进制文件
        with open('E:/image/%d-%d.jpg' % (i,b),"wb") as f:       #建文件
            f.write(image)                                                #写入文件
            print(image_list_name)
        b += 1
    i += 1