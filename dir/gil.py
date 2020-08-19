import time
# from multiprocessing import Process
from threading import Thread

# 求函数运行时间的装饰器
def timeis(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = f(*args,**kwargs)
        end_time = time.time()
        print("运行时间:",end_time - start_time)
        return res
    return wrapper

# 判断一个数是否为质数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

# 自定义线程类
class Prime(Thread):
    def __init__(self,begin,end):
        super().__init__()
        # 求 从begin --end 范围内质数之和
        self.begin = begin
        self.end = end
    def run(self):
        prime = []
        for i in range(self.begin,self.end):
            if isPrime(i):
                prime.append(i)
        print(sum(prime))

# @timeis
# def prime_sum():
#     prime = []
#     # 逐个判断每个数字是不是质数
#     for i in range(1,100001):
#         if isPrime(i):
#             prime.append(i) # 所有质数加入列表
#     print(sum(prime))

# 运行时间: 25.609378814697266
# prime_sum()

@timeis
def thread_4():
    jobs = []
    # 4次循环
    for i in range(1,100001,25000):
        p = Prime(i,i+25000) # 自定义进程类
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]

# 4进程运行时间: 14.834205627441406
# 4线程运行时间: 25.255487203598022
thread_4()

