#!/usr/bin/env python
# coding: utf-8
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
import socket
#import tqdm
import os
import threading

from std_msgs.msg import String
from std_msgs.msg import Int8

def talker():

    #pub = rospy.Publisher('chatter', String, queue_size=10)
    pub_udp = rospy.Publisher('comm_udp', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    # 设置服务器的ip和port
    # 服务器信息
    sever_host = '192.168.155.156'#'192.168.50.65' 
    sever_port = 2000
    print("sever_host")
    print(sever_host)
    print("sever_port")
    print(sever_port)
    # 传输数据间隔符
    SEPARATOR = '<SEPARATOR>'

    # 文件缓冲区
    Buffersize = 1024
    s = socket.socket()
    s.bind((sever_host, sever_port))


    # 设置监听数
    #s.listen(128)
    #print(f'服务器监听{sever_host}:{sever_port}')


    # 接收客户端连接
    #client_socket, address = s.accept()
    # 打印客户端ip
    #print(f'客户端{address}连接')

    while not rospy.is_shutdown():
	s.listen(128)
	client_socket, address = s.accept()
    	# while 1:
        bytes_read = client_socket.recv(Buffersize).decode()
        #        if not bytes_read:
        #            break
        if bytes_read:
	    print(bytes_read)
 	    #pub.publish(bytes_read)
	    pub_udp.publish(bytes_read)
	    if bytes_read == '5':
		print('stop!!')
	
	
        #hello_str = "[udp] hello world %s" % rospy.get_time()
        #rospy.loginfo(hello_str)
        #pub.publish(hello_str)
        rate.sleep()
    client_socket.close()
    s.close()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
