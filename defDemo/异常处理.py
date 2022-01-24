# -*- codeing = utf-8 -*-
# @Time: 2022/1/24 15:18
# @Author: Coisini
# @File: 异常处理.py
# @Software: PyCharm

# 只读模式打开不存在的文件会报错，后面的代码不会再被执行
# f = open("123.txt", "r")
# f.close()

# 异常捕获
import time

try:
    print("---test----")
    f = open("123.txt", "r")
    print("---test----")
    f.close()
except IOError:
    # 捕获异常后执行的代码
    pass

# 捕获异常的名字必须和异常类型一致
try:
    print(num)
except NameError:
    print("产生了错误")

# 也可以捕获多种异常
try:
    print(num)
    f = open("123.txt", "r")
    f.close()
#     把可能出现的问题都放在此处
except (IOError, NameError):
    print("出现了多种错误")

# 打印错误信息
try:
    # print(num)
    f = open("123.txt", "r")
    f.close()
#     把出现的错误以字符串的形式打印出来，打印第一个错误之后就不再执行了
except (IOError, NameError) as result:
    print("出现了多种错误", result)


# 捕获所有的异常
try:
    print(num)
    f = open("123.txt", "r")
    f.close()
#     把出现的错误以字符串的形式打印出来，打印第一个错误之后就不再执行了
except Exception as result:
    print("出现了多种错误", result)


# finally的使用
try:
    f = open("test1.txt", "r")
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")
except Exception as result:
    print("发生异常", result)


