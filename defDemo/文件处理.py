# -*- codeing = utf-8 -*-
# @Time: 2022/1/24 14:58
# @Author: Coisini
# @File: 文件处理.py
# @Software: PyCharm

'''
# 打开文件，w是写模式，文件不存在就新建
f = open("test.txt", "w")

f.write("hello world")
# 关闭文件
f.close()
'''

'''
f = open("test.txt", "r")
# 读五个字符
# content = f.read(5)
# print(content)

# 全部读出来
content = f.readlines()
print(content)

# 读一行
contentLine = f.readline()
print(contentLine)
f.close()

'''

# 使用os模块进行文件操作
import os

os.rename("test.txt", "test1.txt")

