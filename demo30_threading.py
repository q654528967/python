import threading

value = 0


def add_valut():
    global value
    for x in range(1000000):
        value += 1
    print('value:%s' % value)


def main():
    for x in range(2):
        t = threading.Thread(target=add_valut)
        t.start()


if __name__ == '__main__':
    main()
