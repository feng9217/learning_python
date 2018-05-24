from random import choice
print('Choose which way to shoot')
print('left or center or right')

shoot_way = input()
# print('shoot in %s' %shoot_way)
print('shoot in ' + shoot_way)

direction = ['left', 'center', 'right']
saves = choice(direction)
print('Goalkeeper choose ' + saves + ' to save')

# 代码封印 运行直接卡死
# keep_shooting = False
# while keep_shooting == False:
#   if shoot_way == saves:
#     print('oops ...')
#   else:
#     print('go goal go goal !!!')
#     keep_shooting = True