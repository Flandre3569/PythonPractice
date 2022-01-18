# -*- codeing = utf-8 -*-
# @Time: 2022/1/18 14:06
# @Author: Coisini
# @File: 循环语句.py
# @Software: PyCharm

'''
for i in range(5):
    print(i)
'''


'''
# 从0开始到10结束，步进值为3，即为每次加3
for i in range(0, 10, 3):
    print(i)
'''
'''
name = "mingxuan"
for x in name:
    print(x)
'''

name = "mingxuan"
for x in name:
    print(x, end="\t")

print("\n")

a = ["aa", "bb", "cc", "dd"]
for i in range(len(a)):
    print(i, a[i])