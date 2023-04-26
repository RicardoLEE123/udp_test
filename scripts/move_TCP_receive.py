#!/usr/bin/python
# coding: utf-8
import socket
import tqdm
import os
import threading
 

def received( ):
    # 设置服务器的ip和 port
    # 服务器信息
    sever_host = '192.168.50.19'
    #sever_host = '10.42.0.231'
    sever_port = 2000
    # 传输数据间隔符
    SEPARATOR = '<SEPARATOR>'

    # 文件缓冲区
    Buffersize = 1024
    s = socket.socket()
    s.bind((sever_host, sever_port))
    while 1:
        # 设置监听数
        s.listen(128)
        print(f'服务器监听{sever_host}:{sever_port}')

        # 接收客户端连接
        client_socket, address = s.accept()
        # 打印客户端ip
        print(f'客户端{address}连接')

        # 接收客户端信息
        #filename = client_socket.recv(Buffersize).decode()
        #file_size = client_socket.recv(Buffersize).decode()

        # 获取文件的名字,大小
        #filename = os.path.basename(filename)
        '''print('file_size',file_size)
        try:
            file_size = int(file_size)
            print(file_size)
        except:
            print(type(file_size))'''

        # 文件接收处理
        #progress = tqdm.tqdm(range(file_size), f'接收{filename}', unit='B', unit_divisor=1024, unit_scale=True)

        while 1:
                bytes_read = client_socket.recv(Buffersize)
                if not bytes_read:
                    break
                print(bytes_read)
    client_socket.close()
    s.close()

if __name__ == "__main__":
    while 1:
        received()