# -*- coding: utf-8 -*-
# ======================================
# @File    : yys_bonus.py
# @Time    : 2020/3/23 20:40
# @Author  : Rivarrl
# ======================================

# 阴阳师悬赏封印计算

# 式神拼音
sspy = ["yanmo", "datiangou", "jiutuntongzi", "huangchuanzhizhu",
      "taohuayao", "yinghuayao", "lianyou", "tiaotiaogege",
      "xuenv", "mengpo", "fenghuanghuo", "shimengmo", "haifangzhu",
      "kuileishi", "yaohu", "guinvhongye", "quanshen", "guishihei",
      "guishibai", "xixueji", "gunv", "panguan", "bingyong", "shifagui",
      "hudiejing", "yingcao", "choushizhinv", "duyanxiaoseng", "jiaotu",
      "liyujing", "shantu", "tieshu", "tongnan", "tongnv", "zuofutongzi",
      "yunv", "shantong", "jiumingmao", "limao", "wushizhiling", "tiaotiaomeimei",
      "wugushi", "egui", "guanhu", "yatiangou", "shouwu", "sanweihu", "qingwaciqi",
      "jue", "hetong", "chishe", "tubi", "zhoushen", "tangzhisanyao", "jishenghun",
      "tidengxiaoseng", "tianxieguiqing", "tianxieguihong", "tianxieguihuang",
      "tianxieguilv", "denglonggui", "daomuxiaogui", "heibao", "tiaotiaoquan"]
ss = ["阎魔", "大天狗", "酒吞童子", "荒川之主",
      "桃花妖", "樱花妖", "镰鼬", "跳跳哥哥",
      "雪女", "孟婆", "凤凰火", "食梦貘", "海坊主",
      "傀儡师", "妖狐", "鬼女红叶", "犬神", "鬼使黑",
      "鬼使白", "吸血姬", "骨女", "判官", "兵勇", "食发鬼",
      "蝴蝶精", "萤草", "丑时之女", "独眼小僧", "椒图",
      "鲤鱼精", "山兔", "铁鼠", "童男", "童女", "座敷童子",
      "雨女", "山童", "九命猫", "狸猫", "武士之灵", "跳跳妹妹",
      "巫蛊师", "饿鬼", "管狐", "鸦天狗", "首无", "三尾狐", "青蛙瓷器",
      "觉", "河童", "赤舌", "涂壁", "帚神", "唐纸伞妖", "寄生魂",
      "提灯小僧", "天邪鬼青", "天邪鬼红", "天邪鬼黄", "天邪鬼绿",
      "灯笼鬼", "盗墓小鬼", "黑豹", "跳跳犬"]
# 式神id-拼音，拼音-id
idpy = {i:ss[i] for i in range(len(ss))}
pyid = {ss[i]:i for i in range(len(ss))}

hetong_tower = [
    {
        "提灯小僧": 3,
        "盗墓小鬼": 1,
    }
]