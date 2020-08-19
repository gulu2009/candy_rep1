"""
练习1 : 启动两个分支线程,一个线程打印A-Z 26个字母
另外一个线程打印 1--52  这52个数字
要求打印顺序 是 12A34B56C....5152Z

for x in range(65,91):
    print(chr(x))

提示: 一个程序里也可以有多个锁
"""

from threading import Thread,Lock

lock1 = Lock()
lock2 = Lock()

def print_num():
    for i in range(1,53,2):
        lock1.acquire()
        print(i)
        print(i+1)
        lock2.release()

def print_chr():
    for i in range(65,91):
        lock2.acquire()
        print(chr(i))
        lock1.release()

t1 = Thread(target=print_num)
t2 = Thread(target=print_chr)

lock2.acquire() # 先给下边打印字母上锁

t1.start()
t2.start()
t1.join()
t2.join()


