i = 1
result = 0
while i <= 5:
    if i == 4:
        print(f'吃到第{i}吃饱了')
        i += 1
        break
    elif i == 3:
        print(f'吃到第个{i}有虫子，这个不吃')
        i += 1
        continue
    print(f'吃了第{i}个苹果')
    i += 1

