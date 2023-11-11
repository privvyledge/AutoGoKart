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
	out = []
	while ser.inWaiting() > 0:
		out = ser.readline().strip()
		for elements in out:
			print(elements)
		print("end")
		#out1 = out.partition(b'')
		#print(out1[0])
		
