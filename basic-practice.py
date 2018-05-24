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
def sumup(num1, num2):
  # print(num1)
  # print(num2)
  print(num1 + num2)

def saySomething(someone, something):
  # print(someone)
  # print(something)
  print(someone + ' ' + something)

def mixOutput(num, string):
  print(num)
  print(string)
  print(num, string) # 能正常输出的 为什么不能用 + 拼接 而且还自带空格
  print(str(num) + string) # 千万不要作死 把变量名弄得和转换类型的方法名一样

sumup(1, 2)
saySomething('i', 'love you')
mixOutput(1, '字符串')

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
# 增 list.append(sth)
# 删 del list[index]
# 改 list[index] = sth
# 查 list[index] 直接打印即可
# index可以是 负数 也就是倒数

# list 的 slice 很像js里的 slice
# list[from:to] 其中返回的切片 包括from 不包括to
# list[:to] 从第一个元素开始
# list[from:] 到最后一个元素结束
# list[:] 直接返回一个list的 copy

