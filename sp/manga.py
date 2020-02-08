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
import re
import base64
import time
import random

# 漫画爬虫
# PROBLEMS:
# 1. 存在网络不稳定问题时，程序会在获取图片url阶段卡死，代码已经支持断点续爬，长时间卡住的话，手动中断并重启程序。


############ 参数设定 #############

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


############ 工具方法 #############

def validate_mkdir(path_name):
    if not os.path.exists(path_name):
        os.mkdir(path_name)

def delay(lo, hi):
    t = random.randint(lo * 100, hi * 100) / 100
    time.sleep(t)

############ 主要方法 #############

def mhp_crawl_menu(suffix):
    """
    漫画铺，目录页获取每一话地址
    """
    folder_name = suffix.strip('/').split('/')[-1]
    _path = os.path.join(dest_path, folder_name)
    validate_mkdir(_path)
    _pkl_path = os.path.join(_path, 'menu.pkl')
    if not os.path.exists(_pkl_path):
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
    return {"pkl_path": _pkl_path,
            "folder_path": _path}


def mhp_crawl(suffix):
    """
    漫画铺，从第x话获取所有图片
    """
    path_conf = mhp_crawl_menu(suffix)
    _pkl_path = path_conf["pkl_path"]
    _folder_path = path_conf["folder_path"]
    _cpkd_path = os.path.join(_folder_path, 'content.pkl')
    _cpkd_part_path = _folder_path + '/' + 'content_{}.pkl'
    if not os.path.exists(_cpkd_path):
        with open(_pkl_path, 'rb') as f:
            pkd = pickle.load(f)
        if not pkd: return
        content_pkd = {}
        for p_name, p_href in pkd.items():
            _cpkd_part = _cpkd_part_path.format(p_name)
            if os.path.exists(_cpkd_part):
                with open(_cpkd_part, 'rb') as f:
                    real_urls = pickle.load(f)
            else:
                _url = urls['mhp'] + p_href
                resp_1 = requests.get(_url, headers)
                resp_1.encoding = resp_1.apparent_encoding
                pat = re.compile(r'var qTcms_S_m_murl_e="(.*?)";', re.S)
                qTcms_S_m_murl_e = pat.search(resp_1.text).group(1)
                real_urls_str = base64.b64decode(qTcms_S_m_murl_e).decode()
                real_urls = real_urls_str.split('$qingtiandy$')
                with open(_cpkd_part, 'wb') as f:
                    pickle.dump(real_urls, f)
                delay(0.5, 1.5)
            print(p_name, '图片链接已记录')
            content_pkd[p_name] = real_urls
        with open(_cpkd_path, 'wb') as f:
            pickle.dump(content_pkd, f)
        for p_name, p_href in pkd.items():
            _cpkd_part = _cpkd_part_path.format(p_name)
            os.remove(_cpkd_part)
        print('所有图片链接已缓存')
    else:
        with open(_cpkd_path, 'rb') as f:
            content_pkd = pickle.load(f)
    for p_name, p_pic_urls in content_pkd.items():
        _cur_folder_path = os.path.join(_folder_path, p_name)
        validate_mkdir(_cur_folder_path)
        _pic_path = _cur_folder_path + '/' + '{}.jpg'
        start_idx = len(os.listdir(_cur_folder_path))
        for i in range(start_idx, len(p_pic_urls)):
            _pic_url = p_pic_urls[i]
            resp = requests.get(_pic_url, headers)
            with open(_pic_path.format(i+1), 'wb') as f:
                f.write(resp.content)
            print('当前进度：第{} -- 第{}页'.format(p_name, i+1))
            delay(0.75, 2)


if __name__ == '__main__':
    # 漫画铺爬虫的用法：将suffix替换为想看的漫画的主页url的后缀
    # 声之形
    suffix = "zhiyu/shengzhixing/"
    mhp_crawl(suffix)
