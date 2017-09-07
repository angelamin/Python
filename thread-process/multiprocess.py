#coding:utf-8
from multiprocessing import Process
import os
import time
# 子进程要执行的代码
def run_proc(name):
    time.sleep(2)
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p1 = Process(target=run_proc, args=('test1',))
    p2 = Process(target=run_proc, args=('test2',))
    print 'Process will start.'
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print 'Process end.'
