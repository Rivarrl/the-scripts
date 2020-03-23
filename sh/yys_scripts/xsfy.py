# -*- coding: utf-8 -*-
# ======================================
# @File    : xsfy.py
# @Time    : 2020/3/23 23:42
# @Author  : Rivarrl
# ======================================
# 抓数据：http://www.18183.com/yys/201610/xsfy.html

import requests
from bs4 import BeautifulSoup

url = "http://www.18183.com/yys/201610/xsfy.html"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
resp = requests.get(url, header)
resp.encoding = resp.apparent_encoding
bf = BeautifulSoup(resp.text, 'html.parser')
contents = bf.select('.content .panel')
print(contents)
print(len(contents))
xmxs, ts, yh, yqfy, yyh = contents[:5]
tower = contents[5:]
