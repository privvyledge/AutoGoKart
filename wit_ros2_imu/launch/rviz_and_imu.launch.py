import os

from ament_index_python.packages import get_package_share_directory

from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
# get rviz config file location
	rviz_cfg_path = os.path.join(
		get_package_share_directory('wit_ros2_imu'),
		'imu_visualization.rviz')
		
	# arguments
	with_rviz_param = DeclareLaunchArgument(
		'with_rviz',
		default_value='True',
		description='Launch RVIZ2 in addition to other nodes'
	)
	
	rviz_cfg_path_param = DeclareLaunchArgument(
		'rviz_cfg_path_param',
		default_value=rviz_cfg_path,
		description='Launch RVIZ2 with the specified config file'
	)
	
	# visualization nodes
	rviz_and_imu_node = Node(
		package='wit_ros2_imu',
		executable='wit_ros2_imu',
		name='imu',
		remappings=[('/wit/imu', '/imu/data')],
		parameters=[{'port': '/dev/imu_usb'},
					{"baud": 9600}],
		output="screen",
		arguments=['-d', LaunchConfiguration("rviz_cfg_path_param")],
		condition=IfCondition(LaunchConfiguration('with_rviz'))
	)
	
	rviz_display_node = Node(
		package='rviz2',
		executable="rviz2",
		output='screen',
		arguments=['-d', rviz_cfg_path]
	)
	
	return LaunchDescription(
	[
		with_rviz_param,
		rviz_cfg_path_param,
		rviz_and_imu_node,
		rviz_display_node,
	]
	)
