"""
基于 select 方法的 IO多路复用网络并发
重点代码 !!!
"""
from socket import *
from select import select

# 创建好监听套接字
sockfd = socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)

# 与非阻塞IO配合防止传输过程阻塞
sockfd.setblocking(False)

# 准备IO进行监控
rlist = [sockfd]
wlist = []
xlist = []

# 循环监控IO发生
while True:
    # 开始监控IO
    rs,ws,xs = select(rlist,wlist,xlist)
    # 伴随监控的IO的增多,就绪的IO情况也会复杂
    # 分类讨论 分两类  sockfd（监听套接字，客户端链接了就能触发监听套接字） -- connfd（客户端链接套接字）
    for r in rs:
        # 有客户端连接
        if r is sockfd:
            connfd,addr = r.accept()
            print("Connect from",addr)
            connfd.setblocking(False)
            rlist.append(connfd) # 增加监控，禁止 if 内部写死循环
        else:
            # 某个客户端发消息给我
            data = r.recv(1024).decode()
            if not data:
                #  客户端退出
                rlist.remove(r) # 移除监控
                r.close()
                continue
            print("收到:",data)
            # r.send(b'ok')
            wlist.append(r)

    for w in ws:
        w.send(b'OK')
        wlist.remove(w) # 如果不移除会一直就绪发送



