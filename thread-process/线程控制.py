#coding:utf-8
import threading
import time
def haha(max_num):
    for i in range(max_num):
        time.sleep(1)
        print i
"""
创建一个列表，用于存储要启动多线程的实例
"""
threads=[]
for x in range(3):
    t=threading.Thread(target=haha,args=(5,))
    #把多线程的实例追加入列表，要启动几个线程就追加几个实例
    threads.append(t)
for thr in threads:
    #把列表中的实例遍历出来后，调用start()方法以线程启动运行
    thr.start()
for thr in threads:
    """
    isAlive()方法可以返回True或False，用来判断是否还有没有运行结束
    的线程。如果有的话就让主线程等待线程结束之后最后再结束。
    """
    if thr.isAlive():
        thr.join()

print 'end.....'
