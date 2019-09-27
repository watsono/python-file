#!/usr/bin/env python3
# -*- encoding = "utf-8"
import requests
from bs4 import BeautifulSoup as bs

url = "http://pic.netbian.com/index.html"
response = requests.get(url)
response.encoding = "gbk"
html = response.text
soup = bs(html,'lxml')
print(soup.prettify())
