import threading
from threading import current_thread
import time
import random
from queue import Queue

# 定义队列长度，队列满了便不在生产，一般用作消息服务器，如果消息队列满了，开启新的队列进行存储
queue = Queue(5)


class ProducerThread(threading.Thread):

    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global queue
        while True:
            # 随机选择一个数字
            num = random.choice(nums)
            queue.put(num)
            print("生产者 %s 生产了数据 %s" % (name, num))
            t = random.randint(1, 3)
            time.sleep(t)
            print("生产者 %s 睡眠了 %s 秒" % (name, t))


class ConsumerThread(threading.Thread):

    def run(self):
        name = current_thread().getName()
        global queue
        while True:
            num = queue.get()
            # 此方法已经封装好了线程等待和线程同步的方法
            queue.task_done()
            print("消费者 %s 消耗了数据 %s" % (name, num))
            t = random.randint(1, 5)
            time.sleep(t)
            print("消费者 %s 睡眠了 %s 秒" % (name, t))


Producer1 = ProducerThread()
Producer1.start()

Producer2 = ProducerThread()
Producer2.start()

Consumer1 = ConsumerThread()
Consumer1.start()

Consumer2 = ConsumerThread()
Consumer2.start()

Consumer3 = ConsumerThread()
Consumer3.start()
