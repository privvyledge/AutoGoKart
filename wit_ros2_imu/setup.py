from setuptools import setup
import os, glob

package_name = 'wit_ros2_imu'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' +package_name, ['launch/rviz_and_imu.launch.py']),
        ('share/' +package_name, ['rviz/imu_visualization.rviz'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ZYblend',
    maintainer_email='yzheng6@fsu.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'wit_ros2_imu = wit_ros2_imu.wit_ros2_imu:main'
        ],
    },
)
