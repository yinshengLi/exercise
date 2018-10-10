#__author:iruyi
#date:2018/9/25
import threading
import time
import queue

exitFlag = 0
# 加锁后一个线程执行完，另外一个线程才会执行
class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print('开始线程：'+ self.name)
        process_data(self.name, self.q)
        print('退出线程：' + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print('%s processing %s' % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)


threadList = ['Thread-1', 'Thread-2', 'Thread-3']
nameList = ['One', 'Two', 'Three', 'Four', 'Five']

queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadId = 1

# 创建新线程
try:
    for tName in threadList:
        thread = myThread(threadId, tName, workQueue)
        thread.start()
        threads.append(thread)
        threadId += 1

    # 填充队列
    queueLock.acquire()
    for word in nameList:
        workQueue.put(word)
    queueLock.release()

    #等待队列清空
    while not workQueue.empty():
        pass
    # 通知线程是时候推出
    exitFlag = 1

    #等待所有线程完成
    for t in threads:
        t.join()
    print('exit master thread')
except:
    print('Error:无法启动线程')