# 一个发送HTTP请求的小工具
实现方法：Python

需要库：requests库

## 使用方法
./main.py -u <url> -m <method>

./main.py --url <url> --method <method>

eg:./main.py -u http://localhost/dvwa/vulnerabilities/sqli/ -m POST

## 修改POST的data
在request文件夹下面有一个data文件，修改其中的内容

内容格式：arg1=data1&arg2=data2

## 修改Cookie
在request文件夹下面有一个Cookie.json文件夹，修改其中的内容

内容格式：JSON格式即可

## 备注
后续会对其他渗透工具进行集成，敬请期待（参考Firefox下的HackBar插件做一个在线的渗透工具页面）

