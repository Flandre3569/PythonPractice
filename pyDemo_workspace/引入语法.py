# -*- codeing = utf-8 -*-
# @Time: 2022/1/15 23:22
# @Author: Coisini
# @File: 引入语法.py
# @Software: PyCharm


# 引入随机库
import random
x = random.randint(10, 100)
print(x)

# 使用 from...import 可以从某个模块中导入函数

# 石头剪刀布练习
# 1代表剪刀
# 0代表石头
# 2代表布

i = int(input("请输入石头剪刀布的代表数字: "))
you = random.randint(0, 2)
if i == 0:
    print("i出了石头")
    if you == 0:
        print("你们都出了石头")
    elif you == 1:
        print("you出了剪刀")
        print("i赢了")
    else:
        print("you出了布")
        print("you赢了")
elif i == 1:
    print("i出了剪刀")
    if you == 1:
        print("你们都出了剪刀")
    elif you == 0:
        print("you出了石头")
        print("you赢了")
    else:
        print("you出了布")
        print("i赢了")
elif i == 2:
    print("i出了布")
    if you == 2:
        print("你们都出了布")
    elif you == 1:
        print("you出了剪刀")
        print("you赢了")
    else:
        print("you出了石头")
        print("i赢了")
else:
    print("你输入不合法")
