# -*- coding: utf-8 -*-
# ======================================
# @File    : bilibili_cache_generate
# @Time    : 2020/1/8 15:35
# @Author  : Rivarrl
# ======================================
import os
import argparse

parser = argparse.ArgumentParser(description="Bilibili Cache Generator")
parser.add_argument('--video_dir', default=r'F:\bilibili\61747592', help="视频目录, 以av号文件夹为单位")
args = parser.parse_args()
base_dir = args.video_dir

def generate(dir, files):
    blvs = [e for e in files if e.endswith('.blv')]
    if blvs:
        blv_concat(dir, blvs)
    else:
        m4ss = [e for e in files if e.endswith('.m4s')]
        if m4ss:
            m4s_generate(dir, m4ss)

def blv_concat(dir, blvs):
    blvs.sort(key=lambda x: int(x.split('.')[0]))
    tmp_file = 'tmp.txt'
    with open(tmp_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(['%s\t%s'%('file', os.path.join(dir, e).replace('\\', '/')) for e in blvs]))
    nf = dir.split(os.sep)[-2] + '.mp4'
    os.system('ffmpeg.exe -f concat -safe 0 -i %s -c copy %s' % (tmp_file, os.path.join(base_dir, nf)))
    os.remove(tmp_file)

def m4s_generate(dir, m4ss):
    audio = 'audio.m4s'
    video = 'video.m4s'
    if not audio in m4ss or not video in m4ss: return
    audio_path = os.path.join(dir, audio).replace('\\', '/')
    video_path = os.path.join(dir, video).replace('\\', '/')
    nf = dir.split(os.sep)[-2] + '.mp4'
    os.system('ffmpeg -i %s -i %s -vcodec copy -acodec copy %s' % (audio_path, video_path, os.path.join(base_dir, nf)))

video_dirs = os.listdir(base_dir)
for dn in video_dirs:
    video_dir = os.path.join(base_dir, dn)
    if os.path.isdir(video_dir):
        subs = os.listdir(video_dir)
        for inner in subs:
            inner_dir = os.path.join(video_dir, inner)
            if os.path.isdir(inner_dir):
                files = os.listdir(inner_dir)
                generate(inner_dir, files)

