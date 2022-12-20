#!/usr/bin/env python
# Software License Agreement (BSD License)


## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from geometry_msgs.msg import Twist
from rospy.timer import Timer
from std_msgs.msg import Int8
from std_msgs.msg import String

from enum import Enum
                                                                         
State=Enum('State',('MOVE','STOP'))


twist = Twist()
byte_receive = String()
g_state=State.STOP                                                                            

def subCallback2(byte):
    
    global byte_receive
    byte_receive = byte
    #print(byte_receive)

def control(pub,linear,angular):
    global twist
    twist.linear.x=linear
    twist.angular.z=angular
    pub.publish(twist)
 

def move2(pub):
    control(pub,0.1,0)
    rospy.loginfo('move')

def stopMove2(pub):

    control(pub,0,0)
    rospy.loginfo('stop')


def timeCallback2(event):
    
    #rospy.loginfo("come into timeCallback.....")
 
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
 
    global byte_receive, g_state


    if byte_receive.data == "5":
        control(pub,0,0)
	if g_state==State.STOP:
    	    print(byte_receive)
 	    rospy.loginfo('----------stop')
	    g_state=State.MOVE
    else:
        control(pub,0.1,0)
	if g_state==State.MOVE:
	    print(byte_receive)
 	    rospy.loginfo('----------move')
	    g_state=State.STOP


if __name__ == "__main__":
 
    print("conver comm_udp to cmd_vel")
    print(" comm_udp: 5 for stop")

    rospy.init_node("twist_timer")
 
    sub2 = rospy.Subscriber("comm_udp", String, subCallback2,queue_size=10)
 
    rospy.Timer(rospy.Duration(0.1), timeCallback2, oneshot=False)
    
    rospy.spin()
 
    pass
