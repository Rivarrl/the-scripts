# -*- coding:UTF-8 -*-
import requests
import re
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='BJUT Login')
    parser.add_argument('--login_type', default='v4', help='Login Type: v4 or v6 or v4v6')
    args = parser.parse_args()

    with open('./bjut_login.cfg', 'r', encoding='utf-8') as f:
        x = f.read()
    user, pwd = [e.strip() for e in x.split('\n') if e.strip()]
    url4,url6,urlF = "https://lgn.bjut.edu.cn", "https://lgn6.bjut.edu.cn", "https://lgn.bjut.edu.cn/F.htm"
    urls = {
        "v4": [url4],
        "v6": [url6],
        "v4v6": [url4, url6]
    }
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
    login_data = {"DDDDD":user,
                  "upass":pwd,
                  "0MKKey":"Login"}
    login6_data = {"DDDDD":user,
                  "upass":pwd,
                   "v46s":"0",
                   "v6ip":"",
                   "f4serip":"172.30.201.2",
                   "0MKKey":""}
    g = requests.get(url4, headers= headers)
    g.encoding = 'gb2312'
    title = str(re.findall('<title>(.*?)</title>',g.text,re.S))
    if title[10] == "登":
        s = args.login_type
        if s not in urls:
            print("请输入正确的login_type参数: v4 or v6 or v4v6")
        else:
            for url in urls[s]:
                resp = requests.post(url, data=login6_data, headers=headers)
            print("{}登录{}！".format(s, ["失败", "成功"][resp.status_code == 200 and resp.text.find('You have successfully logged into our system') > -1]))
    elif title[10] == "信":
        r = requests.get(urlF, headers= headers)
        time = str(re.findall("time='(.*?)'",r.text,re.S))
        time = re.sub("\D","",time)
        flow = str(re.findall("flow='(.*?)'",r.text,re.S))
        flow = re.sub("\D","",flow)
        flow = int(flow)
        flow /= 1024
        fee = str(re.findall("fee='(.*?)'",r.text,re.S))
        fee = re.sub("\D","",fee)
        print("注销成功！")
        print("已使用时间 Used time: "+time+" Min")
        print("已使用流量 Used flux: "+"%.2f" %flow+" MByte")
        print("余额 Balance : "+"RMB "+fee)