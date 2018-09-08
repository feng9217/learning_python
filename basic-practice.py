#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print(45678 + 0x12fd2)
# print('learn Python in imooc')
# print(100 < 99)
# print(0xff == 25)
# print(0xff != 25)
# print('100 + 200 =')
# print('hello,', 'python')

# answer = input()
# the_answer = eval(input())
# print(answe
# print(the_answer)

# meidan = '胖猪'
# age = 24
# print("%s 今年 %d 岁啦!" %(meidan, age))

# 方形
# for i in range(0, 5):
#   # print('*', end='')
#   for j in range(0, 5):
#     print('*', end='')
#   print() # 用来换行的

# 三角形
# for i in range(0, 5):
#   # print('*', end='')
#   for j in range(0, i+1):
#     print('*', end='')
#   print() # 用来换行的

# bool类型转换测试
# print(bool(-123))
# print(bool(0))
# print(bool('abc'))
# print(bool('False'))
# print(bool(''))
# 有就是 True 没有就是 False

# 函数 21课内容
# def sumup(num1, num2):
#   # print(num1)
#   # print(num2)
#   print(num1 + num2)

# def saySomething(someone, something):
#   # print(someone)
#   # print(something)
#   print(someone + ' ' + something)

# def mixOutput(num, string):
#   print(num)
#   print(string)
#   print(num, string) # 能正常输出的 为什么不能用 + 拼接 而且还自带空格
#   print(str(num) + string) # 千万不要作死 把变量名弄得和转换类型的方法名一样

# sumup(1, 2)
# saySomething('i', 'love you')
# mixOutput(1, '字符串')

# 只能先定义 后调用 ....
# 不仅函数 变量也一样


# 出现的问题: 代码有白色的框框 百度以后是以为安装了 Anaconda 后的规范检查提示
# 表示你码的bug不符合PEP8规范
# 可以再安装一个 python PEP8 autoformat 插件 使用 ctr+shift+r 来自动规范
# 也可以在 首选项 > package setting > Anaconda > setting user >
# {"anaconda_linting": false}
# ctrl+b 运行
# 需要输入的情况 快捷键F5(已设置)运行

#在 python3 中 要想print不换行 print('content', end='')

# int(x) #把x转换成整数
# float(x) #把x转换成浮点数
# str(x) #把x转换成字符串
# bool(x) #把x转换成bool值

# list常规的操作 概念同js的数组 里面可以放任何元素
# name = ['John Doe', 'Jane Doe', 'Crap Bag']
# 增 list.append(sth)
# 插 list.insert(index, item)
# name.append('Shit')
# name.append(['Holly','Shit'])
# name.append('Holly','Shit') # this is wrong, it only takes one arg
# print(name)
# print(len(name))
# print(name[0])
# print(name[-1])
# 删 del list[index]
# 也可以以用 list.pop(index) 默认是最后一个
# 改 list[index] = item
# 查 list[index] 直接打印即可

# list 的 slice 很像js里的 slice
# list[from:to] 其中返回的切片 包括from 不包括to
# list[:to] 从第一个元素开始
# list[from:] 到最后一个元素结束
# list[:] 直接返回一个list的 copy

# 另一种数据结构 有序列表:元组 tuple
# 一旦初始化就不能修改
# 出于这种数据安全的特性 能替代list的地方 就尽量替代使用tuple
# 但是 tuple 的子元素的子元素是可以变的
# classmate = ('John Doe', 'Jane Doe', 'Crap Bag')
# classmate.append('Dan') # error: 'tuple' object has no attribute 'append'
# print(classmate)
# 但是这玩意儿还有个trap 就是定义只有一个元素的 tuple 时 t=(1) 会产生歧义(算术小括号和tuple的歧义)
# 正确操作:
# t = (1,)
# print(t)

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
# print('ABC'.encode('ascii'))
# print('ABC'.encode('utf-8'))
# print('陶文平'.encode('utf-8')) # 中文不能转码成 ASCII 会报错的
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# str transfer to list
# str.split(默认是空格 可以按需求 '符号' 进行分割 just like js)
# lyric = 'I want something just like this'
# lyric_split = lyric.split()
# print(lyric_split)

# ---------- 条件判断 ----------
# if elif else
# 随机获取整数
# from random import randint
# num = randint(5, 30)
# print(num)
# if num > 17:
#   # print('your age is', num) 两种写法都可以
#   print("your age is %d, you're a adult now" %num)
# else:
#   print('you still are a %d years old 弟弟' %num)
# PS: 如果此处采用手动输入的话 需要先将 输入的值(默认str) -> 整数
# input_item = input()
# input_item = int(input_item)
# print(input_item)

# ---------- 循环 ----------
# for ... in ...
# names = ['utf-8', 'GBK', 'ASCII', 'utf-16']
# for item in names:
#   print(item)
# range() 生成整数数列来配合 for in 进行累加计算
# num_list = range(101)
# print(num_list)
# num_list = list(num_list)
# print(num_list)
# sum = 0
# for item in num_list:
#   sum += item
# print(sum)

# while 带条件的循环
# 计算20以内奇数和
# sum = 0
# n = 20
# if n % 2 != 0:
#   print('n 是奇数')
# else:
#   print('n 是偶数')
#   n = n - 1
# while n > 0:
#   print(n)
#   sum += n
#   n = n - 2
# print(sum)

# while + break 提前跳出循环

# while + continue 跳过当次的循环
