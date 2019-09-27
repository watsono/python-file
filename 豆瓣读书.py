#!/usr/bin/env python3
# -*- coding = utf-8 -*-
import requests
import re            #导入需要的库

def main():
    #模拟浏览器的头
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.400'}

    #创建一个文件，储存数据
    f = open("E:\\Python file\\豆瓣读书.txt",'w',encoding='utf-8')

    type_name = input("please input the type:")
    i = 0                                               #小说页码
    while i <= 382:
        url1 = "https://book.douban.com/tag/"
        url2 = "&type=T"
        x = str(i * 20)
        charapter_url = url1 + type_name+ "?start=" + x + url2                     #构建小说目录界面的URL
        print(charapter_url)

        def charapter_html(url):
            response = requests.get(url,headers = headers)  #模拟浏览器请求
            response.encoding = 'utf-8'                     #定义一个获取网页源代码的函数
            html = response.text
            return html

        def write(word):
            f.write(word)

        html = charapter_html(charapter_url)

        #获取书的所有信息
        books_information = re.findall(r'<div class="info">.*?<a href="(.*?)" title="(.*?)".*?<div class="pub">(.*?)</div>.*?<span class="rating_nums">(.*?)</span>.*?<span class="pl">(.*?)</span>.*?<p>(.*?)</p>',html,re.S)
        j = 1
        for book_information in books_information:
            href = book_information[0]                                           #书的链接
            book_name = book_information[1]                                      #书的名字
            book_info = book_information[2].strip()                              #书的作者、出版社、价格
            book_pf = book_information[3].strip() + book_information[4].strip()  #书的评分
            book_jian = book_information[5].replace('\n','')                     #书的简介

            print("%d-%d" % (i,j))
            write("%d-%d:" % (i,j))
            write("\n")
            write("链接：%s\n" % href)                                           #写入文件
            write("书名：%s\n" % book_name)
            write("书籍信息：%s\n" % book_info)
            write("评分：%s\n" % book_pf)
            write("简介：%s\n\n" % book_jian)
            j += 1
        i += 1
if __name__ == '__main__':
    main()                  #主函数