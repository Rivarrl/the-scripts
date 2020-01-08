### sh
> 一些脚本文件

#### bjut_login.py
> bjut网关的自动登录, 需要自己添加配置文件在文件同一路径下
> 配置文件bjut_login.cfg, 内容第一行用户名(学号), 第二行密码  
> 注意: 保管好自己的配置文件, v6有时候会崩, 崩了直接会报错..

#### touchpadtoggle
> 笔记本触摸板开关脚本, 配合shortcuts快捷键用.  
> 需要自己按照文件位置找两个素材, 分别是触摸板开和触摸板关, 自由发挥吧  
> 需要安装xinput控制触摸板  
> 本机测试成功, Sony Vaio SVF143系, Archlinux + Xfce4 

#### bilibili_cache_generator.py  
> b站安卓客户端缓存文件合并(blv格式 & m4s格式)  
> 用到了ffmpeg.exe, 可到[官网](http://www.ffmpeg.org/download.html)下载
> 把解压后的bin目录添加到系统变量path中
> 生成之后源文件还保留着, 需要手动删除

#### bcg_batch.bat
> 如果你在b站缓存的av号很多, 请用这个批处理文件来统一生成
> 记得修改里面的menu路径

#### multiyys.bat
> 阴阳师客户端实现多开, 就一行, 点几次出几个  
> 注意: 把文件中的client替换成自己的路径

