# -*- coding:utf-8 -*-
# 斐波那契数列
class Fabs(object):
    def __init__(self,max):
        self.max = max
        self.n,self.a,self.b = 0,0,1
    def __iter__(self):
        return self
    def next(self):
        if self.n<self.max:
            r = self.b
            self.a,self.b = self.b,self.b+self.a
            self.n = self.n + 1
            return r
        raise StopIteration()

print Fabs(5)
for key in Fabs(5):
    print key


#python专门为for关键字做了迭代器的语法糖。
#在for循环中，Python将自动调用工厂函数iter()获得迭代器，
#在自动调用next()获取元素，还完成了检查StopIteration异常的工作


#output
#<__main__.Fabs object at 0x1018e3510>
# 1
# 1
# 2
# 3
# 5
