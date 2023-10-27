# AutoGoKart

## How to Run
1. Create your own workspace
```
mkdir -p <WorkSpace>
```
2. Clone package into src
```
cd <WorkSpace>
git clone https://github.com/resilient-autonomous-systems-lab/AutoGoKart.git src
```
3. Register USB ports
```
cd src
sudo chmod 777 bind_usb.sh
sudo sh bind_usb.sh
```
check if the usb ports are binded
```
ll /dev/imu_usb
ll /dev/gps_usb
```
4.1 Run in Docker
- build image from dockerfile
```
docker build . 
```
- build and run container in interactive mode
```
docker run -it --name [container_name] --device /dev/ttyACM0 /dev/imu_usb /dev/gps_usb --mount type=bind,src="$(pwm)",target=/gokart_ws [docke_image_name] bash
```
4. Build packages
Now, you are inside the container, since you bind the workspace, anychange you make in container, it will be refleacted in you workspace, be careful
```
cd /gokart_ws
colcon build
source /Path to gokart_ws/gokart_ws/install/setup.bash
```
5. Run Launch files <br>
   (1) AT9S joystick
   ```
   ros2 run at9s_joy at9s_joy
   ```
   ROStopic:
   - `control_command.header.frame_id`: `at9s_joy`
   - `control_command.point.x`: throttle command (-1: reverse max, 1: forward max)
   - `control_command.point.y`: steering command (-1: right max, 1: left max)

   (2) IMU
   ```
   ros2 launch wit_ros2_imu rviz_and_imu.launch.py
   ```
   (3) GPS
   ```
   ros2 launch nmea_navsat_driver nmea_serial_driver.launch.py
   ```
   To read the data, open another terminal
   ```
   source /Path to WorkSpace/<WorkSpace>/install/setup.bash
   ros2 run nmea_navsat_driver read_lat_long
   ```
   (4) Joystick
   ```
   ros2 run joy
   ros2 run joystick joystick
   ```
   ROStopic:
   - `control_command.header.frame_id`: `at9s_joy`
   - `control_command.point.x`: throttle command (-1: reverse max, 1: forward max)
   - `control_command.point.y`: steering command (-1: right max, 1: left max)
  (5) Command Center
  ```
  <run joystick node or cockpit node>
  ros2 run command_center command_center
  ```
  ROStopic:
   - `sbw_control.header.frame_id`: `sbw_input`
   - `sbw_control.point.x`: steering command (-30: right max, 30: left max)
  
   
## ROS Node - Details

![IMG_0162](https://github.com/Naveenkumarar/AutoGoKart/assets/29993827/5eb8c6c0-c0e8-4dfe-831c-f43d045df81f)

Usage  |  Node number  |  Node Name  |  Topic number  |  Topic Name  |  Msg Type
---  |---  |---  |---  |---  |---
Read Angle from SBW Encoder  |  5  |  gokart_sbw  |    |  sbw_feedback  |   geometery_msgs/msg/PointStamped
Send Steering Angle To SBW Encoder  |  5  |  gokart_sbw  |   2  |  sbw_control  |   geometery_msgs/msg/PointStamped
Read Steering Control And Throttle Control from Computer/ Controller  |  7  | gokart_command  |  1  |  control_command  |  geometery_msgs/msg/PointStamped
Send JoyStick(Gamepad) To Command Extractor  |  3  |  gokart_joystick  |  4   |  joystick_command  |   sensor_msgs/msg/joy
Send Cockpit To Command Extractor  |  2  |  gokart_cockpit  |  5   |  cockpit_command  |   geometery_msgs/msg/PointStamped





 

