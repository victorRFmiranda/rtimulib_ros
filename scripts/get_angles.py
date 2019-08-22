#!/usr/bin/env python
import rospy
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from sensor_msgs.msg import Imu
import numpy as np



IMU = Imu()

def callback_imu(msg):
	global IMU
	IMU = msg
	quat = [IMU.orientation.x, IMU.orientation.y, IMU.orientation.z, IMU.orientation.w]
	euler = euler_from_quaternion(quat)
	degree = np.rad2deg(euler)
	print degree



def main():
	rospy.init_node("Imu_Reader")
	#while not rospy.is_shutdown():
	rospy.Subscriber("/rtimulib_node/imu", Imu, callback_imu)
	rospy.spin()
	

if __name__ == '__main__':
	try:
		main();
	except rospy.ROSInterruptException:
		pass
