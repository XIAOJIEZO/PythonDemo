import threading
import time
from threading import current_thread


def myThread(arg1, arg2):
    print(current_thread().getName(), "start")
    print("%s %s" % (arg1, arg2))
    time.sleep(1)
    print(current_thread().getName(), "stop")


# 依次调用函数，顺序执行
# for i in range(1, 6, 1):
#     t1 = myThread(i, i + 1)


# 多线程运行
for i in range(1, 6, 1):
    # t1 = myThread(i, i + 1)
    # target传入函数名，args传入参数
    t1 = threading.Thread(target=myThread, args=(i, i + 1))
    t1.start()

print(current_thread().getName(), "end")

"""
Thread-1 start
1 2
Thread-2 start
2 3
Thread-3 start
3 4
Thread-4 start
4 5
Thread-5 start
5 6
MainThread end
Thread-3 stop
Thread-2 stop
Thread-1 Thread-4 stop
stop
Thread-5 stop

并行运行，每个线程之间并未等待一秒，主线程先结束，希望主线程先结束，需要线程同步，一个线程运行的时候能够等待另一个线程结束
"""