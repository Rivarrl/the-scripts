# -*- coding: utf-8 -*-
# ======================================
# @File    : generate_json.py
# @Time    : 2020/3/27 17:00
# @Author  : Rivarrl
# ======================================
from bs4 import BeautifulSoup
import pickle

def fxmxs():
    a = xmxs.select('.panel-content .clx .gl-cl')
    print(a)
    dxmxs = {}
    for i in range(2, len(a), 2):
        k, v = a[i], a[i+1]
        print(k.get_text() + '\t' + v.get_text())
        dxmxs[k.get_text()] = v.get_text()
    with open('./data/xmxs.pkl', 'wb') as f:
        pickle.dump(dxmxs, f)

def fts():
    dts = {}
    chapters = ts.select('.panel-content .cp')
    for i, ch in enumerate(chapters):
        ch_name = ch.select_one('.tb-hd').get_text()
        results = ch.select('.clx')
        for r in results:
            cell = r.select('.tb-cl')
            k = cell[0].get_text()
            v = cell[1].get_text()
            # print(k, '\t', v)
            dts['[' + ch_name + '] ' + k] = v
    print(dts)
    with open('./data/ts.pkl', 'wb') as f:
        pickle.dump(dts, f)


def fyh_yyh():
    # 御魂和业原火
    dyh = {}
    results = yh.select('.panel-content .cp')
    r2 = yyh.select('.panel-content .cp')
    results += r2
    for i, x in enumerate(results):
        k = x.select_one('.tb-hd').get_text()
        details = x.select('.clx .tb-r')
        v = []
        for p in details:
            v += [p.get_text()]
        v = ' '.join(v)
        dyh[k] = v
    print(dyh)
    with open('./data/yh.pkl', 'wb') as f:
        pickle.dump(dyh, f)


def fyqfy():
    dyqfy = {}
    results = yqfy.select('.panel-content .cp')
    for i, x in enumerate(results):
        k = x.select_one('.tb-hd').get_text()
        details = x.select('.clx .tb-r')
        v = []
        for p in details:
            v += [p.get_text()]
        v = ' '.join(v)
        dyqfy[k] = v
    print(dyqfy)
    with open('./data/yqfy.pkl', 'wb') as f:
        pickle.dump(dyqfy, f)


def ftower():
    dtower = {}
    for each in tower:
        title = each.select_one('.panel-head').get_text()
        dtower[title] = {}
        lvs = each.select('.panel-content .cp')
        for i, x in enumerate(lvs):
            k = x.select_one('.tb-hd').get_text()
            details = x.select('.clx .tb-r')
            v = []
            for p in details:
                v += [p.get_text()]
            v = ' '.join(v)
            dtower[title][k] = v
    print(dtower)
    with open('./data/tower.pkl', 'wb') as f:
        pickle.dump(dtower, f)


def gen():
    """
    缺少26~28章探索，地鬼4君子，皮肤塔（青行灯以后的），魂土
    需要手动补上
    """
    path = './data/{}.pkl'



if __name__ == '__main__':
    f = open('./data/18183.pkl', 'rb')
    hs = pickle.load(f)
    f.close()
    bf = BeautifulSoup(hs, 'html.parser')
    contents = bf.select('.content .panel')
    xmxs, ts, yh, yqfy, yyh = contents[:5]
    tower = contents[5:]
    # fxmxs()
    # fts()
    # fyh_yyh()
    # fyqfy()
    # ftower()
    gen()