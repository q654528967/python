import random
computer = random.randint(0, 2)
user = int(input('0--石头，1--剪刀，2--布'))
if ((computer == 0) and (user == 2)) or ((computer == 1) and (user == 0)) or ((computer == 2) and (user == 0)):
    print('玩家胜利')
elif computer == user:
    print('平局')
else:
    print('电脑胜利')
print(computer)
