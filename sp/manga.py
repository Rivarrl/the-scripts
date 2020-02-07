# -*- coding: utf-8 -*-
# ======================================
# @File    : manga.py
# @Time    : 2020/2/6 15:02
# @Author  : Rivarrl
# ======================================
import os
import requests
from bs4 import BeautifulSoup
import pickle
# 漫画爬虫

# 保存路径
dest_path = "D:/data/manga"
# 记录一些漫画网址
urls = {}
# 漫画铺
urls['mhp'] = "https://www.manhuapu.com"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}
html_parser = 'html.parser'

def mhp_crawl_menu(suffix):
    folder_name = suffix.strip('/').split('/')[-1]
    _path = os.path.join(dest_path, folder_name)
    if not os.path.exists(_path):
        os.mkdir(_path)
    _pkl_path = os.path.join(_path, 'menu.pkl')
    if os.path.exists(_pkl_path):
        return _pkl_path
    _html_path = os.path.join(_path, 'menu.html')
    if os.path.exists(_html_path):
        with open(_html_path, 'r', encoding='utf-8') as f:
            resp_text = f.read()
    else:
        _url = urls['mhp'] + '/' + suffix
        resp = requests.get(_url, headers)
        resp.encoding = resp.apparent_encoding
        resp_text = resp.text
        with open(_html_path, 'w', encoding='utf-8') as f:
            f.write(resp_text)
    bf = BeautifulSoup(resp_text, html_parser)
    links_a = bf.select('#play_0 > ul > li > a')
    pkd = {}
    for a in links_a:
        p_name = a.get_text()
        p_href = a.get('href')
        pkd[p_name] = p_href
    with open(_pkl_path, 'wb') as f:
        pickle.dump(pkd, f)
    return _pkl_path


def mhp_crawl(suffix):
    _pkl_path = mhp_crawl_menu(suffix)
    with open(_pkl_path, 'rb') as f:
        pkd = pickle.load(f)
    if not pkd: return
    for p_name, p_href in pkd.items():
        print(p_name, p_href)
        _url = urls['mhp'] + p_href
        _url_p = lambda x: _url + '?p={}'.format(x)
        resp_1 = requests.get(_url, headers)
        resp_1.encoding = resp_1.apparent_encoding
        bf_1 = BeautifulSoup(resp_1.text, html_parser)
        options = bf_1.select('#k_pageSelect')
        pages = options[-1].get('value')
        print(pages)
        break

if __name__ == '__main__':
    # 声之形
    suffix = "zhiyu/shengzhixing/"
    mhp_crawl(suffix)
