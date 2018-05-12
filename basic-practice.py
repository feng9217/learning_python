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

meidan = '胖猪'
age = 24
print("%s 今年 %d 岁啦!" %(meidan, age))

# 方形
for i in range(0, 5):
  # print('*', end='')
  for j in range(0, 5):
    print('*', end='')
  print() # 用来换行的

# 三角形
for i in range(0, 5):
  # print('*', end='')
  for j in range(0, i+1):
    print('*', end='')
  print() # 用来换行的


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