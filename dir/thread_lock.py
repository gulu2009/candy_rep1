"""
线程锁演示
"""
from  threading import Thread,Lock

lock = Lock() # 锁对象
a = b = 0

def value():
    while True:
        lock.acquire()
        if a != b:
            print("a = %f,b = %f"%(a,b))
        lock.release()

t = Thread(target=value)
t.start()

while True:
    with lock:   # 上锁
        a += 0.1
        b += 0.1
                 # with语句块结束自动解锁


t.join()