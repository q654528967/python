import random
li1 = [[], [], []]
tch = ['ss', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg']
for i in tch:
    li1[random.randint(0, 2)].append(i)
print(li1)
