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

# 查
# musicName = input("请输入查找音乐的名字:")
musicName = "七号公园"
if musicName in musicList:
    print("存在")
else:
    print("不存在")

wordList = ["a", "b", "c", "a", "d"]
# 查找指定目标范围的元素，并返回查找到的元素下标
# 范围是左闭右开
# 找不到会报错，可以通过捕获错误让程序继续执行
print(wordList.index("a", 1, 4))

# 统计某个元素出现几次
print(wordList.count("a"))

# 列表翻转,会修改列表本身
wordList.reverse()
print(wordList)

# 排序，升序
wordList.sort()
print(wordList)

# 排序，降序
wordList.sort(reverse=True)
print(wordList)

schoolList = [["清华大学", "北京大学"], ["山东大学", "中国海洋大学"], ["武汉理工大学", "武汉大学"]]
print(schoolList[0])


# 综合小题目: 三个办公室，7个老师，把7个老师随机分配到3个办公室中
import random

offices = [[], [], []]
teachers = ["A", "B", "C", "D", "E", "F", "G"]

for teacher in teachers:
    index = random.randint(0, 2)
    offices[index].append(teacher)

i = 1
for office in offices:
    print("办公室%d的人数为: %d" % (i, len(office)))
    i += 1
    for name in office:
        print("办公室的老师有: %s" % name, end='\t')
    print('\n')
    print('--' * 20)
