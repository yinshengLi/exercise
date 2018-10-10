#__author:iruyi
#date:2018/9/25
import threading
import time

exitFlag = 0
# 加锁后一个线程执行完，另外一个线程才会执行
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print('开始线程：'+ self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 5)
        # 释放锁，开启下一个线程
        threadLock.release()
        print('退出线程：' + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print('%s: %s' % (threadName,time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建两个线程
try:
    thread1 = myThread(1, 'Thread-1', 1)
    thread2 = myThread(2, 'Thread-2', 2)

    #start
    thread1.start()
    thread2.start()

    # 添加线程到线程列表
    threads.append(thread1)
    threads.append(thread2)

    #等待所有线程完成
    for t in threads:
        t.join()
    print('exit master thread')
except:
    print('Error:无法启动线程')
