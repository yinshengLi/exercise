#__author:iruyi
#date:2018/9/25
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    host = socket.gethostname()
    port = 9999
    s.connect((host, port))

    s.send('你是个。。。'.encode('utf-8'))

    # 接收小于 1024 字节的数据
    msg = s.recv(1024)
    s.close()
    print(msg.decode('utf-8'))
except Exception as e:
    print('连接失败:',e)
    sys.exit(0)