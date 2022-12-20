#!/usr/bin/env python
# Software License Agreement (BSD License)


## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from geometry_msgs.msg import Twist
from rospy.timer import Timer
from std_msgs.msg import Int8
                                                                         

twist = Twist()
byte_receive = 0

def subCallback2(byte):
    
    global byte_receive
    byte_receive = byte
 
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
    
    rospy.loginfo("come into timeCallback.....")
 
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
 
    global byte_receive
    if byte_receive == '5':
        control(pub,0,0)
 	rospy.loginfo('----------stop')
    else:
        control(pub,0.1,0)
	rospy.loginfo('----------move')


if __name__ == "__main__":
 
    rospy.init_node("twist_timer")
 
    sub2 = rospy.Subscriber("comm_udp", Int8, subCallback2,queue_size=10)
 
    rospy.Timer(rospy.Duration(0.1), timeCallback2, oneshot=False)
    
    rospy.spin()
 
    pass
