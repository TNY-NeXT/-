import os
import time
from multiprocessing import Process


def info(title):
    print(title)
    print('module name:', __name__)  # __main__ 等于 __main__
    print('parent process', os.getppid())  # 第一次调用该函数输出的主进程为pycharm，pycharm本身也是一个进程
    print('process id', os.getpid())    # 该函数运行时的进程号


def f(name):
    pass


if __name__ == '__main__':
    info('\033[32;1m main process line \033[0m')  # 这段代码是执行 info 函数，怪不得输出两个结果
    time.sleep(0.2)
    # 只要先执行一个info进程，那么后面创建的任何info进程都是第一个info进程的子进程
    p1 = Process(target=info, args=('yanhuo',))
    p2 = Process(target=info, args=('nayi',))
    p3 = Process(target=info, args=('nayi',))
    p1.start()
    p2.start()
    p3.start()
    p3.join()

# 输出结果是一个函数的父进程，其他并行执行的函数都是子进程，并不是迭代地生成父进程和子进程
