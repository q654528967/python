import threading
import time


def coding():
    for x in range(3):
        print('正在写代码%s' % threading.current_thread())
        time.sleep(1)


def drawing():
    for x in range(3):
        print('正在画图%s' % threading.current_thread())
        time.sleep(1)


def main():
    ti = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)
    ti.start()
    t2.start()
    print(threading.enumerate())


if __name__ == '__main__':
    main()

