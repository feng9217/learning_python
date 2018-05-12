while_i = 0
while_sum = 0
while_sumflag = False

print('while 循环')
while while_sumflag == False:
  if while_i < 101:
    while_sum = while_sum + while_i
    # i ++ 竟然不能这样用 ...
    while_i = while_i + 1
  if while_i == 101:
    while_sumflag = True
    print(while_i)
    print(while_sum)

print('for 循环')
for_sum = 0
for i in range(1, 101):
  for_sum = for_sum + i
print(for_sum)
