#!/usr/bin/env python
import roslib
import rospy
import std_msgs.msg

kLifterMoterTopicName = "robot/lifter_motor"
kFrontMoterControllerTopicName = "/agv2/rod_front_joint_position_controller/command"
kRearMoterControllerTopicName = "/agv2/rod_rear_joint_position_controller/command"

class base_topic_subscriber(object):
    def __init__(self, topic_name, topic_type):
        self.topic_name_ = topic_name
        self.topic_type_ = topic_type
        self.base_sub_ = rospy.Subscriber(\
          self.topic_name_, self.topic_type_, self.Callback)
    def Callback(self, ros_base_msg):
        self.base_msg_ = ros_base_msg
        self.CallbackHook()
    def CallbackHook(self):
        rospy.logwarn("Not implemnted {} subscriber hook yet!!".format(topic_name))

class lifter_sub(base_topic_subscriber):
    def __init__(self, topic_name):
         super(lifter_sub, self).__init__(topic_name, std_msgs.msg.UInt8)
         self.front_pub_ = rospy.Publisher(kFrontMoterControllerTopicName, std_msgs.msg.Float64, queue_size=2)
         self.rear_pub_ = rospy.Publisher(kRearMoterControllerTopicName, std_msgs.msg.Float64, queue_size=2)
         self.lifter_up_val_ = 0.1
         self.lifter_down_val_ = 0.0
    def CallbackHook(self):
        _cmd = self.base_msg_.data
        front_up_flag = (_cmd & 0x0f)
        rear_up_flag = (_cmd & 0xf0)
        front_checker = front_up_flag  & 0x0e
        rear_checker = rear_up_flag & 0xe0
        msg = std_msgs.msg.Float64()
        if ((front_checker == 0) and (rear_checker == 0)):
            if front_up_flag != 0:
                msg.data = self.lifter_up_val_
                self.front_pub_.publish(msg)
            else:
                msg.data = self.lifter_down_val_
                self.front_pub_.publish(msg)
            if rear_up_flag != 0:
                msg.data = self.lifter_up_val_
                self.rear_pub_.publish(msg)
            else:
                msg.data = self.lifter_down_val_
                self.rear_pub_.publish(msg)
        else:
            rospy.logwarn("command to topic {} error".format(self.topic_name_))


if __name__ == "__main__":
    try:
        rospy.init_node('tapping_lifter')
        lifter = lifter_sub(kLifterMoterTopicName)
        rospy.spin()
    except rospy.ROSInterruptException:
        print "ros exception"
        pass
