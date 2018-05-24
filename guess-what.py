from random import randint
num = randint(5, 30)

print('guess the number picked by random')
bingo = False

# if version

# while bingo == False: #bingo 为 false 的时候就循环执行
#   answer = eval(input())
#   if answer < num:
#     print('%d is too small' %answer)
#   elif answer > num:
#     print('%d is too big' %answer)
#   else:
#     print('bingo!!')
#     bingo = True

# 在python3中 通过input()输入得到的都是一个 String, 不能直接和Number比较
# 所以需要输入时就进行转义 number = eval(input())

# the other version made by function
def equalOrnot(num1, num2):
  if num1 < num2:
    print('too small')
    return False
  if num1 > num2:
    print('too big')
    return False
  if num1 == num2:
    print('bingo')
    return True

while bingo == False:
  answer = eval(input()) # 因为传进函数后的值存在比较 所以不能是 str 和 num 比较
  bingo = equalOrnot(answer, num)