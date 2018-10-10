#__author:iruyi
#date:2018/9/25
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999
# 绑定端口号
s.bind((host,port))
# 设置最大连接数，超过后排队
s.listen(5)
print('等待连接--')

while True:

    clientsocket,addr = s.accept()
    print("连接地址: %s" % str(addr))
    message = clientsocket.recv(1024)
    print('接收信息：', message.decode('utf-8'))

    msg = 'welcome to my test'
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()