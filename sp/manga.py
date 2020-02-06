# -*- coding: utf-8 -*-
# ======================================
# @File    : manga.py
# @Time    : 2020/2/6 15:02
# @Author  : Rivarrl
# ======================================
import os
import requests
from bs4 import BeautifulSoup

# 漫画爬虫

# 保存路径
dest_path = "D:/data/manga"
# 记录一些漫画网址
urls = {}
# 漫画铺
urls['mhp'] = "https://www.manhuapu.com/"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}

def mhp_crawl(suffix):
    folder_name = suffix.strip('/').split('/')[-1]
    _path = os.path.join(dest_path, folder_name)
    if not os.path.exists(_path):
        os.mkdir(_path)
    t = '1.html'
    if os.path.exists(t):
        with open(t, 'r', encoding='utf-8') as f:
            resp_text = f.read()
    else:
        _url = urls['mhp'] + suffix
        resp = requests.get(_url, headers)
        resp.encoding = resp.apparent_encoding
        resp_text = resp.text
        with open(t, 'w', encoding='utf-8') as f:
            f.write(resp_text)
    bf = BeautifulSoup(resp_text, 'html.parser')
    links_li = bf.select('#play_0 > ul > li')
    for li in links_li:
        print(li)

if __name__ == '__main__':
    # 声之形
    suffix = "zhiyu/shengzhixing/"
    mhp_crawl(suffix)