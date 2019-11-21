#!/usr/bin/env python3
# -*- coding = utf-8 -*-
import requests
import re
import matplotlib.pyplot as plt


commodity = input("please input the commodity's name:") # 输入需要搜索的商品信息
page = int(input('please input the page:'))
url1 = 'https://s.taobao.com/search?q='
url2 = '&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190831&ie=utf8&bcoffset=4&p4ppushleft=%2C48&s=' # 组成url
url3 = '&ntoffset=4'

def main():
    # 登录信息
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
               'Cookie':'自己的cookie信息'} # 自己修改cookie信息

    i = 1
    j = 1
    a = 0
    b = 0   # 统计四个段商品的数量
    c = 0
    d = 0
    dic = {}
    commodity_infoss = []
    while j <= page:
        num = str((j - 1) * 44)
        url = url1 + commodity + url2 + num + url3

        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        html = response.text
        j+=1

        commodity_infos = re.findall(r'"raw_title":"(.*?)".*?view_price":"(.*?)".*?item_loc":"(.*?)".*?"view_sales":"(.*?)人付款".*?"nick":"(.*?)"',html,re.S)

        commodity_infoss = commodity_infoss + commodity_infos

    commodity_infoss.sort(key=lambda x:float(x[1]),reverse=1) # 排序从大到小
    max = float(commodity_infoss[0][1])                      # 价格最高的商品
    m4 = max/4                                               # 最高价格的四分之一
    m2 = max/2                                               #最高价格的二分之一
    m3 = (max/4)*3                                           #最高价格的四分之三
    print("价格最贵的几个显卡为：")
    for commodity_info in commodity_infoss:
        num = float(commodity_info[1])
        if num>0 and num<=m4:
            a = a+1
        elif num>m4 and num<=m2:
            b = b+1                                   # 根据分的四段，计算每一段商品的数量
        elif num>m2 and num<=m3:
            c = c+1
        elif num and num<=max:
            d = d+1


        if i<6:
            print(commodity_info)    # 输出价格最贵的几个显卡
        i = i+1

        if commodity_info[2] not in dic:
            dic[commodity_info[2]] = 1      # 计算每个发货地出现的次数
        else:
            dic[commodity_info[2]] = dic[commodity_info[2]] + 1



    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体


    dict = tuple(dic.keys())   # 取出字典中的地名
    nums = tuple(dic.values())  # 取出字典中的地名出现次数


    def draw(dic, number):
        input_values = (dic)  # 指定输入参数
        squares = (number)  # 指定输出参数

        plt.rcParams['savefig.dpi'] = 300  # 图片像素
        plt.rcParams['figure.dpi'] = 500  # 分辨率

        plt.xticks(rotation=90)

        plt.bar(input_values, squares, linewidth=3)  # 调用绘制函数，传入输入参数和输出参数
        plt.title("%s发货地分布" % commodity, fontsize=24)  # 指定标题，并设置标题字体大小
        plt.xlabel("发货地", fontsize=10)  # 指定X坐标轴的标签，并设置标签字体大小
        plt.ylabel("频率", fontsize=14)  # 指定Y坐标轴的标签，并设置标签字体大小

        plt.tick_params(axis='both', labelsize=10)  # 参数axis值为both，代表要设置横纵的刻度标记，标记大小为10
        plt.show()  # 打开matplotlib查看器，并显示绘制的图形

    draw(dict, nums)
    print("价格0-%.2f的显卡数量为：%d" % (m4,a))
    print("价格%.2f-%.2f的显卡数量为：%d" % (m4,m2,b))
    print("价格%.2f-%.2f的显卡数量为：%d" % (m2, m3,c))
    print("价格%.2f-%.2f的显卡数量为：%d" % (m3, max, d))




if __name__ == '__main__':
    main()
