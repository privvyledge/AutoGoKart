# AutoGoKart

## How to Run
1. Create your own workspace
```
mkdir -p <WorkSpace>
```
2. Clone package into src
```
cd <WorkSpace>
git clone https://github.com/ZYblend/AutoGoKart.git src
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
4. Build packages
Notice, make sure you return to the workspace, don't run `colcon build` in src
```
cd ..
colcon build
source /Path to WorkSpace/<WorkSpace>/install/setup.bash
```
5. Run Launch files <br>
   (1) IMU
   ```
   ros2 launch wit_ros2_imu rviz_and_imu.launch.py
   ```
   (2) GPS
   ```
   ros2 launch nmea_navsat_driver nmea_serial_driver.launch.py
   ```
   To read the data, open another terminal
   ```
   source /Path to WorkSpace/<WorkSpace>/install/setup.bash
   ros2 run nmea_navsat_driver read_lat_long
   ```
