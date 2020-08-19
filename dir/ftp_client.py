"""
ftp 客户端
"""
from socket import *

# 服务器地址
ADDR = ('127.0.0.1',8888)

# 具体的请求方法
class FTPClient:
    def __init__(self,sock):
        self.sock = sock

    def 请求查看(self):
        pass

# 网络连接启动程序
def main():
    sock = socket()
    sock.connect(ADDR) # 建立网络连接

    # 通过对象调用类中具体方法完成请求
    ftp = FTPClient(sock)

    # 循环输入命令
    while True:
        print("""
        ========== 命令选项 ===========
                    list
                  get file
                  put file
                    exit
        ==============================
        """)
        cmd = input("命令:")
        if cmd == 'list':
            ftp.请求查看()
