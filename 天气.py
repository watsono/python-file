#!/usr/bin/env python3
# -*- coding = utf-8 -*-

import requests
import re

url = "http://www.weather.com.cn/weather/101220101.shtml"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}

response = requests.get(url,headers=headers)
response.encoding = 'utf-8'
html = response.text

weathers = re.findall(r'class="sky skyid lv.*?<h1>(.*?)<.*?<p.*?>(.*?)<.*?tem">(.*?)</p>',html,re.S)
for weather in weathers:
    print(weather[0])
    print(weather[1])
    print(weather[2].replace('<i>','最低气温为').replace('</i>','').replace('<span>','最高气温为').replace('</span>/',','))
    print('\n')
