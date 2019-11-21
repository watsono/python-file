#!/usr/bin/env python3
# -*- coding = "utf-8" -*-
import requests
import re

def main():
    url_basic = 'https://accounts.douban.com/j/mobile/login/basic'        #post请求发送的date
    url = 'https://www.douban.com/'
    headers = { "User-Agent":'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'}#浏览器信息
    data = {
        'ck': '',
        'name': '用户名',
        'password': '密码',                   #豆瓣账户信息
        'remember': 'false', # 是否记住密码
        'ticket': ''
    }

    s = requests.session()
    s.post(url_basic, headers=headers, data=data)   #post传入数据，登录
    response = s.get(url, headers=headers)          #获取登录后的界面
    response.encoding = 'utf-8'
    html = response.text
    text_list = re.findall(r'<div class="text">.*?>(.*?)</a>(.*?)</div>.*?<div class="title">.*?<a href="(.*?)".*?>(.*?)</a>.*?<p>(.*?)</p>',html,re.S) #正则表达式匹配结果
    for text_info_list in text_list:
        name = text_info_list[0]
        word = text_info_list[1].strip().replace('\n','')
        word = name + word
        herf = text_info_list[2]
        title = text_info_list[3]
        infor = text_info_list[4]
        print(word,herf,title,infor)

if __name__ == '__main__':
    main()                        #主函数
