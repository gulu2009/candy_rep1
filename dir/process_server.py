"""
多进程并发网络模型
重点代码!!!

步骤思路
    创建网络套接字用于接收客户端请求
    等待客户端连接
    客户端连接，则创建新的进程具体处理客户端请求
    主进程继续等待其他客户端连接
    如果客户端退出，则销毁对应的进程
"""

from socket import *
from multiprocessing import  Process
from signal import *

# 全局变量定义地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

# 具体处理客户端请求 函数结束即客户端退出
def handle(connfd):
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b'OK')
    connfd.close()

def main():
    # 创建tcp套接字
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)

    # 处理僵尸进程
    signal(SIGCHLD,SIG_IGN)

    print("Listen the port %d..."%PORT)
    while True:
        # 循环接收端连接
        try:
            connfd,addr = sock.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            sock.close()
            return

        # 创建新的进程,处理客户端具体请求事务
        p = Process(target=handle,args=(connfd,))
        p.daemon = True
        p.start()

if __name__ == '__main__':
    main()