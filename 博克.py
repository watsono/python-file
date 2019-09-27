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
               'Cookie':'cna=HAauFcFY2xoCASQHM5adoovj; t=74bd027388e6a20f9ca00aae6002c05c; '
                        'isg=BNTUgu0_dcLa7OHsBrmykBlRphKGhfh-DCmROG61bN_iWXSjljghp-fbWZHkujBv; '
                        'l=cBIlkfSHqa5avcKsBOCwquI8aO7TjIOYYuPRwNVXi_5dE6L_sLbOk7aSDFp6csWdTGLB450m8ze9-etkiKy06Pt-g3fP.; '
                        'uc3=vt3=F8dBy3zdlK2cNikfUMI%3D&id2=VyyX4U0dFoSkYA%3D%3D&nk2=FPjAYXgwUOI%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; tracknick=watsooon; '
                        'lgc=watsooon; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; '
                        'enc=UEMVhtlmnrUJpQ1OoqJfjOY72p8%2BW3Or3rJNyFjFc1wKgLNAzCtr411BFet3pasaUlZXbrdLs47mvNcfffSn2Q%3D%3D; miid=915240311857798560; '
                        'thw=cn; UM_distinctid=16c033696d1102-011bdd2d22c227-4c312272-1fa400-16c033696d2345; '
                        'x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; '
                        'cookie2=7cccf262f9d938ec638cb27d82df0ca4; v=0; _tb_token_=e5f37574365e3; uc1=cookie14=UoTaHPCCA4tVfQ%3D%3D; '
                        'mt=ci=-1_0; JSESSIONID=7E7BB91527A01257027752D0AC65B734; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; '
                        'hng=CN%7Czh-CN%7CCNY%7C156; swfstore=113178'}

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

