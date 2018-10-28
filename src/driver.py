#!/usr/bin/env python

import os
import time

from dual_g2_hpmd_rpi import motors, MAX_SPEED

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class Driver():
    r = 0.192 / 2 # wheel radius [m]
    d = 0.50 / 2 # half distance between wheels [m]
  
    def __init__(self):
        rospy.init_node('listener', anonymous=True)

        self.cmdvel_sub = rospy.Subscriber("/cmd_vel", Twist, self.cmdvel_cb)
        
        motors.enable()
        motors.setSpeeds(0, 0)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()
        
    def cmdvel_cb(self, message):
        print(message.linear.x, message.angular.z)
        omega_l = (message.linear.x - d*message.angular.z) / self.r
        omega_r = (message.linear.x + d*message.angular.z) / self.r
        print(omega_l, omega_r)
        


if __name__=="__main__":
    driver = Driver()