import threading
import random
import time

gMoney = 1000
gCondition = threading.Lock()
gTotalTimes = 10
gTimes = 0


class Producer(threading.Thread):
    def run(self):
        global gMoney, gTimes, gTotalTimes
        while True:
            money = random.randint(100, 1000)
            gCondition.acquire()
            if gTimes >= gTotalTimes:
                gCondition.release()
                break
            gMoney += money
            print('%s生产了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gMoney))
            gTimes += 1
            gCondition.release()
            time.sleep(1)


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100, 1000)
            gCondition.acquire()
            if gMoney >= money:
                gMoney -= money
                print('%s消费者消费了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gMoney))
            else:
                if gTimes >= gTotalTimes:
                    gCondition.release()
                    break
                print('%s消费者将要消费%d元钱，剩余%d元钱，余额不足' % (threading.current_thread(), money, gMoney))
            gCondition.release()
            time.sleep(1)


def main():
    for x in range(3):
        t = Producer(name='生产者线程%d' % x)
        t.start()

    for x in range(5):
        t = Consumer(name='消费者线程%d' % x)
        t.start()


if __name__ == '__main__':
    main()



