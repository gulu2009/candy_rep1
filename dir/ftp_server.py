"""
文件服务器 服务端程序
"""

from socket import *
from threading import Thread

# 全局变量定义地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

# 具体处理客户端请求
class FTPServer(Thread):
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__()

    def 查看方法(self):
        pass

    # 处理客户端   总分模型部分
    def run(self):
        while True:
            # 接收某个客户端的所有请求
            data = self.connfd.recv(1024)
            if data == "查看":
                self.查看方法()
            elif data == "下载":
                pass

        self.connfd.close()

# 创建多线程并发模型
def main():
    # 创建tcp套接字
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)

    print("Listen the port %d..."%PORT)
    while True:
        # 循环接收端连接
        try:
            connfd,addr = sock.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            sock.close()
            return

        # 创建新的线程,处理客户端具体请求事务
        t = FTPServer(connfd)
        t.setDaemon(True)
        t.start()

if __name__ == '__main__':
    main()