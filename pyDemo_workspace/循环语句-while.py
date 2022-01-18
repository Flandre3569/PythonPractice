# -*- codeing = utf-8 -*-
# @Time: 2022/1/18 14:19
# @Author: Coisini
# @File: 循环语句-while.py
# @Software: PyCharm

'''
i = 0
while i < 5:
    print("当前是第%d次循环" % (i + 1))
    print("i=%d" % i)
    i += 1
'''

# 1-100求和
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

count = 0
while count < 5:
    print(count, "小于5")
    count += 1
else:
    print(count, "大于或等于5")


# 九九乘法表 for版本
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d * %d = %d" % (i, j, i*j), end='\t')
    print("\n")


# 九九乘法表 while版本
x = 1
y = 1
while x <= 9:
    while y <= x:
        print("%d * %d = %d" % (x, y, x * y), end='\t')
        y += 1
    x += 1
    y = 1
    print('\n')
