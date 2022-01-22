# -*- codeing = utf-8 -*-
# @Time: 2022/1/22 22:35
# @Author: Coisini
# @File: 函数初使用.py
# @Software: PyCharm

# 函数的定义
def printInfo():
    print("--" * 20)
    print("人生苦短，我用python")
    print('--' * 20)


# 函数调用
printInfo()


# 带参数和返回值的函数
def addNum(a, b):
    c = a + b
    return c


num = addNum(1, 2)
print(num)


# 返回多个值，直接返回即可
def divid(a, b):
    shang = a // b
    yushu = a % b
    return shang, yushu


sh, ys = divid(10, 3)
print("商为: %d" % sh, "余数为: %d" % ys)


def printRaw(rawNum):
    i = 1
    while i <= rawNum:
        print('--' * 20)
        i += 1

printRaw(3)


def operSum(a, b, c):
    addSum = a + b + c
    return addSum

def operAvg(a, b, c):
    avg = operSum(a, b, c) / 3
    return avg

print(operAvg(1, 2, 3))


# 局部范围内使用全局变量
a = 200
def printNum():
    # 此时标注了a是使用的全局变量，所以修改这个数值，会影响全局定义的变量，不会单独生成局部变量
    global a
    print(a)
    a = 300

printNum()

print(a)
