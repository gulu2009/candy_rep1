"""
多线程并发网络模型
重点代码!!!
"""

from socket import *
from threading import  Thread

# 全局变量定义地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

# 具体处理客户端请求
class MyThread(Thread):
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__()

    # 处理客户端
    def run(self):
        while True:
            data = self.connfd.recv(1024)
            if not data:
                break
            print(data.decode())
            self.connfd.send(b'OK')
        self.connfd.close()

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
        t = MyThread(connfd)
        t.setDaemon(True)
        t.start()

if __name__ == '__main__':
    main()