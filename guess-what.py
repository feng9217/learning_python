from random import randint
num = randint(5, 20)

print('guess the number picked by random')
bingo = False

while bingo == False:
  answer = eval(input())
  if answer < num:
    print('%d is too small' %answer)
  if answer > num:
    print('%d is too big' %answer)
  if answer == num:
    print('bingo!!')
    bingo = True

# 在python3中 通过input()输入得到的都是一个 String, 不能直接和Number比较
# 所以需要输入时就进行转义 number = eval(input())