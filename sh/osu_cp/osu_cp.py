# -*- coding: utf-8 -*-
# ======================================
# @File    : osu_cp.py
# @Time    : 2020/8/5 0:43
# @Author  : Rivarrl
# ======================================
import os
import shutil
from collections import defaultdict

songs_path = "D:/game/osu!/Songs"

sd = {'k': 1024, 'm': 1024 * 1024}
class Format:
    def __init__(self, fmt, output, size_limit=None):
        self.fmt = fmt
        self.output = output
        if size_limit:
            if size_limit[-1].lower() in sd:
                size_limit = int(size_limit[:-1]) * sd[size_limit[-1]]
            else:
                size_limit = int(size_limit)
        self.size_limit = size_limit

    def cp(self, ori, format, dest_name):
        if not format in self.fmt: return
        if self.size_limit:
            sz = os.path.getsize(ori)
            if sz < self.size_limit: return
        dest_path = os.path.join(self.output, "{}.{}".format(dest_name, format))
        if not os.path.exists(dest_path):
            shutil.copy(ori, dest_path)

# 格式，根据需要酌情添加
song_fmt = {"mp3", "wav", "ogg"}
video_fmt = {"mp4", "flv", "avi"}
pic_fmt = {"jpg", "jpeg", "png"}

# 输出文件夹
output = "D:/data/pyout/osu_cp/"
song_output, video_output, pic_output = ["song", "video", "pic"]

sf = Format(song_fmt, os.path.join(output, song_output), size_limit='1m')
# vf = Format(video_fmt, os.path.join(output, video_output), size_limit='1m')
pf = Format(pic_fmt, os.path.join(output, pic_output), size_limit='100k')

fd = (sf, pf)

def ckmkdir(x):
    if not os.path.exists(x):
        os.mkdir(x)
# 建立文件夹
ckmkdir(output)
for x in (song_output, video_output, pic_output):
    y = os.path.join(output, x)
    ckmkdir(y)

# 统计格式
format_map = defaultdict(int)
al = os.listdir(songs_path)
n = len(al)
for i, x in enumerate(al):
    song_p = os.path.join(songs_path, x)
    for y in os.listdir(song_p):
        f = os.path.join(song_p, y)
        if not os.path.isfile(f): continue
        fmt = y.split('.')[-1].lower()
        format_map[fmt] += 1
        dest_name = song_p.split(os.sep)[-1].split(" ", 1)[-1]
        for ff in fd:
            ff.cp(f, fmt, dest_name)
    print('\rplease wait: {:.2f}%...'.format((i+1)*100/n), end='', flush=True)
# print(format_map)
