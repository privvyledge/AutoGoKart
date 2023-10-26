import time
import serial

ser = serial.Serial( port = '/dev/ttyACM0',baudrate=115200)

ser.isOpen()

while 1:
	out = ''
	while ser.inWaiting() > 0:
		out += str(ser.readline(),encoding='utf-8')
	
	
	if out != '':
		print(out)
		spl = out.split(",")
		for k in spl:
			print(k)
		
