# -*- codeing = utf-8 -*-
# @Time: 2022/1/20 17:19
# @Author: Coisini
# @File: 列表.py
# @Software: PyCharm

# 空链表
# nameList = []

nameList = ["小王", "小张", "小红"]
print(nameList[1:])

# 混合列表,初始设置的是什么类型，那么数组中存储的就是什么类型
mixList = [1, "张三"]
print(mixList)
print(type(mixList[0]))
print(type(mixList[1]))

for name in nameList:
    print(name)

i = 0
while nameList:
    print(nameList[i])
    i += 1