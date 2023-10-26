echo "start copy imu_usb.rules to /etc/udev/rules.d/"
sudo cp wit_ros2_imu/imu_usb.rules /etc/udev/rules.d
echo "start copy gps_usb.rules to /etc/udev/rules.d/"
sudo cp nmea_navsat_driver/gps_usb.rules /etc/udev/rules.d

service udev reload
sleep 2
service udev restart
echo "Finish!!!"
