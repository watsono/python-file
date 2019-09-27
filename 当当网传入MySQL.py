#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
import re               #传入库
import pymysql

def main():
    i = 1
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}

    url_1 = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-all-0-0-1-"
    while i <= 25:
        dd_url = url_1 + str(i)

        response = requests.get(dd_url,headers = headers)
        response.encoding = "gbk"
        html = response.text

        book_lists = re.findall(r'<div class="name">.*?<a href="(.*?)".*?title="(.*?)">',html,re.S)
        print(i)
        for book_list in book_lists:
            book_href = book_list[0]
            book_name = book_list[1]
            db = pymysql.connect("116.62.245.119", "admin", "123456", "dangdang")
            cursor = db.cursor()
            insert_sql = (
                "REPLACE INTO book_bookinfo(btitle,bdate)" "VALUES(%s,%s)")#插入数据，replace和insert区别
            data_sql = (book_name,book_href)

            cursor.execute(insert_sql, data_sql)#插入数据
            db.commit()

        i += 1

if __name__ == '__main__':
    main()
