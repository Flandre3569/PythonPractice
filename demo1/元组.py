# -*- codeing = utf-8 -*-
# @Time: 2022/1/22 21:50
# @Author: Coisini
# @File: 元组.py
# @Software: PyCharm

'''
# 创建空的元组
tup1 = ()

# 一个数据的元组，注意需要添加逗号，来标识这个数据是个元组类型
tup2 = (50,)
print(type(tup2))

# 多个数据的元组
tup3 = (10, 20, 30)
print(type(tup3))
'''


# 增
# 使用合并元组的形式
tup2 = (12, 17, 19)
tup3 = ("abc", "xyz", "was")
tup = tup2 + tup3
print(tup)

# 删
# 整体删除，不能删除单个元素
del tup2

# 改  元组不允许修改，所以直接不能修改

# 查
tup1 = ('abc', 'def', 1000, 200)
print(tup1[0])
print(tup1[-1])
print(tup1[1: 5])  # 左闭右开
