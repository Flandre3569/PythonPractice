# -*- codeing = utf-8 -*-
# @Time: 2022/1/20 21:15
# @Author: Coisini
# @File: 数据增删改查.py
# @Software: PyCharm

nameList = ["小王", "小张", "小李"]

# append 增
for name in nameList:
    print(name, end='\t')
print('\n')

# addName = input("请输入要增加的学生姓名:")
# 末尾增加一个元素
# nameList.append(addName)

for name in nameList:
    print(name, end='\t')

print('\n')

a = [1, 2]
b = [3, 4]
# 把b当做一个整体添加到a
a.append(b)
# extend 增
# 把b扩展后添加到a中
a.extend(b)
print(a)


# insert 增
x = [0, 1, 2]
# 指定下标插入位置
x.insert(1, 3)
print(x)

# 删
movieName = ["钢铁侠", "蜘蛛侠", "美国队长", "奇异博士"]
# 删除指定位置元素
del movieName[1]
print(movieName)

# 弹出最后一个元素
# movieName.pop()
# print(movieName)

# 通过value值删除元素，如果有两个相同的元素时，只删除第一个
movieName.remove("钢铁侠")
print(movieName)


# 改
musicList = ["七号公园", "温泉", "不谈恋爱", "放空"]
musicList[1] = "不说再见"
print(musicList)
