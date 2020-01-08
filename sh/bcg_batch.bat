@echo off
set menu=F:\bilibili
for /D %%s in (%menu%\*) do (
echo %%s
python bilibili_cache_generator.py --video_dir=%%s
)