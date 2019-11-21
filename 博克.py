#!/usr/bin/env python3
# -*- coding = utf-8 -*-
import requests
import re
import operator
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show

commodity = input("please input the commodity's name:") # 输入需要搜索的商品信息
page = int(input('please input the page:'))
url1 = 'https://s.taobao.com/search?q='
url2 = '&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190814&ie=utf8&bcoffset=4&p4ppushleft=%2C48&s=' # 组成url
url3 = '&ntoffset=4'

def main():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
               'Cookie':'自己的cookie信息'}

    j = 1
    dic = {}
    while j <= page:
        num = str((j - 1) * 44)
        url = url1 + commodity + url2 + num + url3
        print(url)
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        html = response.text
        j+=1

        commodity_info_titles = re.findall(r'"raw_title":"(.*?)"',html,re.S)
        commodity_info_prices = re.findall(r'"view_price":"(.*?)"',html,re.S)
        commodity_info_sales = re.findall(r'"view_sales":"(.*?)"',html,re.S)
        commodity_info_nicks = re.findall(r'"nick":"(.*?)"',html,re.S)
        commodity_infos_locs = re.findall(r'"item_loc":"(.*?)"',html,re.S)

        for commodity_info_loc in commodity_infos_locs:
            if commodity_info_loc not in dic:
                dic[commodity_info_loc] = 1
            else:
                dic[commodity_info_loc] =dic[commodity_info_loc] + 1
        dic.items()

        swd = sorted(dic.items(),key=operator.itemgetter(1),reverse=True)


    dict = tuple(dic.keys())
    nums = tuple(dic.values())

    # prepare some data
    x = [1,2,3,4,5,6,7,8,9,10,11]
    y = nums

    # output to static HTML file
    output_file("lines.html")

    # create a new plot with a title and axis labels
    p = figure(title="数量", x_axis_label='x', y_axis_label='y')

    # add a line renderer with legend and line thickness
    p.line(x, y, legend="Temp.", line_width=2)

    # show the results
    show(p)
    print(x)
    print(y)

if __name__ == '__main__':
    main()

