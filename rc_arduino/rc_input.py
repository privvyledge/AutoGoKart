import time
import serial

def isint(num):
	try:
		int(num)
		return True
	except ValueError:
		return False

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
			print(isint(k));
			if isint(k):
				k = 1-2*(int(k)-1000)/(2000-1000)
				print(k)
		
