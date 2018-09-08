# shoot once
# from random import choice
# print('Choose which way to shoot')
# print('left or center or right')

# shoot_way = input()
# # print('shoot in %s' %shoot_way)
# print('shoot in ' + shoot_way)

# direction = ['left', 'center', 'right']
# saves = choice(direction)
# print('Goalkeeper choose ' + saves + ' to save')

# 代码封印 运行直接卡死
# keep_shooting = False
# while keep_shooting == False:
#   if shoot_way == saves:
#     print('oops ...')
#     keep_shooting = False
#   else:
#     print('go goal go goal !!!')
#     keep_shooting = True

# 记录得分
from random import choice

score_you = 0
score_com = 0
direction = ['left','center','right']

for i in range(8):
  print('==== Round %d - You Kick ====' %(i+1))
  print('choose one side to shoot:')
  print('left, center, right')
  you = input()
  print('you kick ' + you)
  com = choice(direction)
  print('computer saved ' + com)
  if you !=com:
    print('goal!')
    score_you += 1
  else:
    print('shit')
    score_com += 1
  print('score %d(you) - %d(com)\n' %(score_you, score_com))