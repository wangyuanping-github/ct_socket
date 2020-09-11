# -*- coding: UTF-8 -*-

import socket
import time
# 建立一个服务端
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',6789)) #绑定要监听的端口
server.listen(5) #开始监听 表示可以使用五个链接排队
xml_address="server.xml"
conn,addr = server.accept() #等待链接,多个链接的时候就会出现问题,其实返回了两个值
print(conn,addr)

while True:# conn就是客户端链接过来而在服务端为期生成的一个链接实例
    while True:
        print ('开始等待')
        res = conn.recv(80)  # 接受报文头
        cmds = res.decode('utf-8')
        print(cmds)
        with open(xml_address, mode='wb') as f:
            line =conn.recv(1024)
            f.write(line)
            break
    print('完成传输')
    print('开始发送回复文档')
    for i in range(2):
        Packet_header = "NTCTTP/1.0 NOTIFY(CRLF)Content-Type:text/xml(CRLF)Content-Length:456(CRLF)(CRLF)"
        pkgHead = Packet_header.encode('utf8')
        conn.sendall(pkgHead)
        with open('ctHeartBeatRequest.xml', mode='rb') as f:
            buf = f.read(1024)
            conn.sendall(buf)
        time.sleep(1)
    print('回复文档传输成功')
conn.close()