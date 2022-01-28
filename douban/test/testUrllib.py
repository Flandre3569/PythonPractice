# -*- codeing = utf-8 -*-
# @Time: 2022/1/28 20:51
# @Author: Coisini
# @File: testUrllib.py
# @Software: PyCharm

import urllib.request
import urllib.parse
# 通过get获取一个网页
'''
response = urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode("utf-8"))  # 对获取到的网页进行utf8解析
'''

# post请求
'''
data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
response = urllib.request.urlopen("http://httpbin.org/post", data=data)
print(response.read().decode("utf-8"))
'''

# 超时处理
'''
try:
    response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
    print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("请求超时")
'''

# 请求头
'''
response = urllib.request.urlopen("http://www.baidu.com")
# 请求请求头所有信息
# print(response.getheaders())
# 请求单个信息
print(response.getheader("Content-Type"))
'''

# 模拟浏览器发送数据
'''
url = "http://httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}
data = bytes(urllib.parse.urlencode({"name": "mingxuan"}), encoding="utf-8")
req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
'''

url = "https://douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}

req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))