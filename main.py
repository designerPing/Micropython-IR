# main.py -- put your code here!
import pyb
from pyb import Pin
import time
import micropython



def send_id(out_signal ,pin_name):

	L2 = Pin(pin_name, mode=Pin.AF_PP, af=Pin.AF1_TIM2)
	timer = pyb.Timer(2,freq = 38000)

	ch = timer.channel(1, pyb.Timer.PWM, pin =L2, pulse_width_percent = 0.5)
	pyb.udelay(9000)
	
	ch = timer.channel(1, pyb.Timer.PWM, pin =L2, pulse_width_percent = 0)
	pyb.udelay(4500)

	for i in out_signal:
		if i == "0":
			ch = timer.channel(1, pyb.Timer.PWM, pin =L2, pulse_width_percent = 0.5)
			pyb.udelay(560)
			ch = timer.channel(1, pyb.Timer.PWM, pin =L2, pulse_width_percent = 0)
			pyb.udelay(565)
			
		else:
			ch = timer.channel(1, pyb.Timer.PWM, pin =L2, pulse_width_percent = 0.5)
			pyb.udelay(560)
			ch = timer.channel(1, pyb.Timer.PWM, pin =L2, pulse_width_percent = 0)
			pyb.udelay(1690)
			
		ch = timer.channel(1, pyb.Timer.PWM, pin =L2, pulse_width_percent = 0.5)
		pyb.udelay(560)
		ch = timer.channel(1, pyb.Timer.PWM, pin =L2, pulse_width_percent = 0)
			

# send_id("11001101001100100111001110001100",'PA5')




def read_id(pin_name):

	L1 = Pin(pin_name, Pin.IN, Pin.PULL_UP)

	a = []

	while L1.value() == 1:
		pass

	pyb.udelay(13560)	# this for initial time

	for i in range(1000):		
		v = L1.value()
		a.append(v)
		pyb.udelay(56)
	# print (a, len(a))

	a_c = []
	count = 0

	for i in a:	
		if i == 1:
			count += 1

		elif i == 0:
			if count > 0 :
				a_c.append(count)
			count =0

	for i in range(len(a_c)):
		if a_c[i] > 10:
			a_c[i] = "1"
		else:
			a_c[i] = "0"
	# print (a_c)

	B1 = "".join(a_c)
	# convert into string
	# print (B1)

	Data_device = B1[0:16]
	# print (Data_device)
	# Device ID

	Data_buttom = str(B1[16:32])
	# print (Data_buttom)
	# Buttom ID

	Device_dict = {"1100110100110010":"TV"}

	Buttom_dict = { "0111001110001100":"OK" ,
					"0101001110101100": "UP",
				 	"0100101110110100":"DOWN",
				 	"1001100101100110":"LEFT",
				 	"1000001101111100":"RIGHT"}

	for key_d in Device_dict.keys():
		if  str(Data_device) == str(key_d):
			# print (str(Data_device),"  ", str(key_d))
			print (Device_dict[key_d], end = ' ')
	# print ("hh")
	if Data_buttom in Buttom_dict.keys():
		# print (Data_buttom)
		print(Buttom_dict[Data_buttom])
	return B1

while True:
	f = read_id("PC1")
	send_id(f)
