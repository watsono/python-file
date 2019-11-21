#!/usr/bin/env python3
# -*- coding = utf-8 -*-
import requests
import re
import operator
import matplotlib.pyplot as plt

commodity = input("please input the commodity's name:") # 输入需要搜索的商品信息
page = int(input('please input the page:'))
url1 = 'https://s.taobao.com/search?q='
url2 = '&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190814&ie=utf8&bcoffset=4&p4ppushleft=%2C48&s=' # 组成url
url3 = '&ntoffset=4'

def main():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
               'Cookie':'cookies信息（浏览器中查找自己的）'}

    j = 1
    dic = {}
    while j <= page:
        num = str((j - 1) * 44) #需要爬取的页数
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
    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

    dict = tuple(dic.keys())
    nums = tuple(dic.values())

    input_values = (dict)  # 指定输入参数
    squares = (nums)  # 指定输出参数

    plt.rcParams['savefig.dpi'] = 300  # 图片像素
    plt.rcParams['figure.dpi'] = 500  # 分辨率

    plt.xticks(rotation=90)

    plt.bar(input_values, squares, linewidth=3)  # 调用绘制函数，传入输入参数和输出参数
    plt.title("%s发货地分布" % commodity, fontsize=24)  # 指定标题，并设置标题字体大小
    plt.xlabel("发货地", fontsize=10)  # 指定X坐标轴的标签，并设置标签字体大小
    plt.ylabel("频率", fontsize=14)  # 指定Y坐标轴的标签，并设置标签字体大小

    plt.tick_params(axis='both', labelsize=10)  # 参数axis值为both，代表要设置横纵的刻度标记，标记大小为10
    plt.show()  # 打开matplotlib查看器，并显示绘制的图形

if __name__ == '__main__':
    main()







