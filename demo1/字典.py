# -*- codeing = utf-8 -*-
# @Time: 2022/1/22 22:06
# @Author: Coisini
# @File: 字典.py
# @Software: PyCharm


# 字典的定义形式，类似于json对象格式
info = {"name": "zhangsan", "age": 18}

# 字典的访问
print(info)
print(info["name"])
print(info["age"])

# 访问了不存在的键值，直接访问会报错
# 如果使用get访问，如果key值不存在，则会显示未找到，而不是报错使程序崩溃，默认返回none
print(info.get("mingxuan"))

# 自定义未找到的返回值
print(info.get("mingxuan", "未找到key值"))

# 增
newId = 1
info["id"] = newId
print(info["id"])

'''
# 删
# del 删除
print("删除前: %s" % info)
del info["name"]
print("删除后: %s" % info)
# clear 清空
print("清空前: %s" % info)
info.clear()
print("清空后: %s" % info)
'''


# 改
info["name"] = "mingxuan"
print(info)

# 查
for item in info:
    print(item)

print(info.keys())  # 得到所有的键，得到的是一个数组
print(info.values())  # 得到所有的值，得到的也是一个数组
print(info.items())  # 得到每一个键值对， 得到的也是一个数组

# 使用循环
for key, value in info.items():
    print(key, value)

# 枚举类型,可以直接得到元素的下标
numList = [123, 23, 42, 17]
for i, x in enumerate(numList):
    print(i, x)

# 集合的使用，进行去重操作
numList = [1, 1, 2, 2, 3]
print(numList)
num = set(numList)
print(num)

