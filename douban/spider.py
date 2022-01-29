# -*- codeing = utf-8 -*-
# @Time: 2022/1/28 20:40
# @Author: Coisini
# @File: spider.py
# @Software: PyCharm
import urllib.request
from bs4 import BeautifulSoup
import re


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 爬取网页获取的内容
    dataList = getData(baseurl)

    # 保存数据
    savePath = ".\\豆瓣电影Top250.xls"
    # saveData(savePath)


findLink = re.compile(r'<a href="(.*?)">')  # 生成正则表达式对象
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)


# 爬取网页 获取数据
def getData(baseurl):
    dataList = []
    for i in range(0, 1):
        url = baseurl + str(i * 25)
        html = askUrl(url)  # 获取到的单个网页源码
    # 解析数据
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('div', class_="item"):    # 查找符合要求的字符串，形成列表
        data = []  # 保存一部电影的全部信息
        item = str(item)
        print(item)
        break
        link = re.findall(findLink, item)[0]   # 使用正则表达式查找指定的字符串
        print(link)
    return dataList


# 得到指定一个url的网页内容
def askUrl(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    }
    # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接受什么水平的分件）
    request = urllib.request.Request(url, headers=head)
    html = ""

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

def saveData(savePath):
    print("save...")

if __name__ == '__main__':
    main()
