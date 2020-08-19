"""
select 方法示例
"""
from select import *
from socket import *
import time

# 准备点IO
f = open('test.log')

sockfd = socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)

sock = socket(AF_INET,SOCK_DGRAM)
sock.bind(('0.0.0.0',9999))

time.sleep(5)


print("开始监控IO")
rs,ws,xs = select([sockfd],[],[])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)


