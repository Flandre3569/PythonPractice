# -*- codeing = utf-8 -*-
# @Time: 2022/1/29 10:55
# @Author: Coisini
# @File: testBs4.py
# @Software: PyCharm

from bs4 import BeautifulSoup
file = open('./easy表格变色.html', "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")

# 得到tag，标签及其内容
# print(bs.table)

# 直接获取到标签里的内容
# print(bs.title.string)

# 获取标签的属性值，类似于class、name、id等
# print(bs.td.attrs)

# BeautifulSoup表示整个文档
# print(type(bs))


# --------------------------------------

# 文档的遍历
# print(bs.head.contents[1])

# 文档的搜索

# 字符串过滤: 会查找与字符串完全匹配的内容
# t_list = bs.find_all("td")
# print(t_list)

# 正则表达式搜索: 使用search()方法来匹配内容
# import re
# t_list = bs.find_all(re.compile("t"))
# print(t_list)

# 传入一个函数，根据函数的要求来搜索，可以自定义搜索内容
def name_is_exists(tag):
    return tag.has_attr("name")

t_list = bs.find_all(name_is_exists)

print(t_list)