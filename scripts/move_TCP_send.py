
#!/usr/bin/python
# coding: utf-8

import socket
#import tqdm
import os


def send(content):
    SEPARATOR = '<SEPARATOR>'
    host = '192.168.1.7'
    #host = '10.42.0.1'
    port = 2000

    s = socket.socket()
    print(f'服务器连接中{host}:{port}')
    s.connect((host, port))
    print('与服务器连接成功')

    s.send(content.encode())
    s.close()

if __name__ == "__main__":
    while 1:
        send("1")
