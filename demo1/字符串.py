# -*- codeing = utf-8 -*-
# @Time: 2022/1/20 16:50
# @Author: Coisini
# @File: 字符串.py
# @Software: PyCharm

'''
word = '字符串'
sentence = "这是一个句子"
paragraph = """
    这是一个段落的标题
    这是一个段落的第一段
    这是一个段落的第二段
"""

print(word)
print(sentence)
print(paragraph)
'''

# 内部包含需要转义
my_str = 'I\'m student'
print(my_str)
my_str_simple = "I'm student"
print(my_str_simple)

my_str_simple2 = 'Jason says "I am student"'
print(my_str_simple2)

# 输出index为0-5元素
print(my_str_simple[0:6])
print(my_str_simple[0:6:2])

# 简写
print(my_str_simple[4:])
print(my_str_simple[:6])

# 技巧，字符串可以和乘法配合使用
print("--" * 30)

# '\' --> 转义字符
print("hello\nworld")
# 如果在字符串前加r，那么字符串中的任何转义字符都会失效，进行正常输出
print(r"hello \n world")

