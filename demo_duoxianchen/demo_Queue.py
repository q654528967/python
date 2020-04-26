import threading
from queue import Queue
import time


# q.put('x')
# q.put('y')
# q.put(3)
# q.put(4)
# print(q.full())
# for x in range(4):
#     print(q.get())


def set_value(q):
    index = 0
    while True:
        q.put(index)
        index += 1
        time.sleep(3)


def get_value(q):
    while True:
        print(q.get())
        print(q.full())


def main():
    q = Queue(4)
    t1 = threading.Thread(target=set_value, args=[q])
    t2 = threading.Thread(target=get_value, args=[q])
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
