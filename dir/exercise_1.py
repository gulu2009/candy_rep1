"""
练习: 模拟自动窗口售票系统
10个窗口,同时售票,一个线程表示一个窗口
一共有500张票, 放在列表中记做T1--T500,
要求按照顺序卖出(打印 w1---T305)
每次买一张票会有 0.1s停顿
编程模拟这个事情
"""

from threading import Thread
from time import sleep

ticket = ["T%d" % x for x in range(1, 501)]

# 模拟卖票 w 表达窗口
def sell(w):
    while ticket:
        print("%s 窗口卖出:%s"%(w,ticket.pop(0)))
        sleep(0.1)

jobs = []
for i in range(1,11):
    t = Thread(target = sell,args=("w%d"%i,))
    jobs.append(t)
    t.start()

[i.join() for i in jobs]