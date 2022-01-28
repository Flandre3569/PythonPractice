# -*- codeing = utf-8 -*-
# @Time: 2022/1/28 20:40
# @Author: Coisini
# @File: spider.py
# @Software: PyCharm


def main():
    baseurl = "https://movie.douban.com/top250?start=?"
    # 爬取网页获取的内容
    dataList = getData(baseurl)

    # 保存数据
    savePath = ".\\豆瓣电影Top250.xls"
    saveData(savePath)
# 爬取网页 获取数据
def getData(baseurl):
    dataList = []
    # 解析数据
    return dataList

def saveData(savePath):
    print("save...")

if __name__ == '__main__':
    main()
