import RPi.GPIO as GPIO
import datetime
import csv
import time
import sys
import Adafruit_DHT
from ina219 import INA219, DeviceRangeError
from time import sleep
from datetime import datetime

#----------GPIO SETTINGS------------
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()
#-----------HEATING PIN SETTINGS------------
heatPIN = 14
GPIO.setup(heatPIN, GPIO.OUT)
#-----------FAN PIN SETTINGS------------
fanPIN = 15
GPIO.setup(fanPIN, GPIO.OUT)
#-----------FAN PIN SETTINGS------------
minifanPIN = 18
GPIO.setup(minifanPIN, GPIO.OUT)

#----------INA SETTING------------
SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 2.0
ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS)
ina.configure(ina.RANGE_16V)
#-----------Global Var-------------------------
fanStatus = 0
heatStatus = 0
time_interval = 1
now = datetime.now()

fname = "result"+ str(now.month) + str(now.day) + ".csv"

def main():  
	f = open(fname,"w",newline="")
	csv_writer = csv.writer(f)
	csv_writer.writerow(['Time','Humidity','Temperature','Voltage','fan','heat'])
	f.close()
	while True:
		#get the data
		H, T = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302,'4')
		bus_voltage = ina.voltage()
		now = datetime.now()
		currentTime = str(now.month) +"/" + str(now.day) +" " + str(now.hour) + ":" + str(now.minute)

#check the condition
		if(T < 15):
			GPIO.output(fanPIN, GPIO.HIGH)
			GPIO.output(heatPIN, GPIO.LOW)
			GPIO.output(minfanPIN, GPIO.LOW)
			fanStatus = 0
			heatStatus = 1
			print("T < 15")
		elif(T > 35):
			GPIO.output(fanPIN, GPIO.LOW)
			GPIO.output(heatPIN, GPIO.HIGH)
			GPIO.output(minifanPIN, GPIO.LOW)
			fanStatus = 1
			heatStatus = 0
			print("T > 35")

		else:
			if(H < 60):
				GPIO.output(fanPIN, GPIO.HIGH)
				GPIO.output(heatPIN, GPIO.HIGH)
				GPIO.output(minifanPIN, GPIO.HIGH)
				fanStatus = 0
				heatStatus = 0
				print("15 < T < 35, H < 60")
			else:
				GPIO.output(fanPIN, GPIO.LOW)
				GPIO.output(heatPIN, GPIO.HIGH)
				GPIO.output(minifanPIN, GPIO.LOW)
				fanStatus = 1
				heatStatus = 0
				print("15 < T < 35, H > 60")
#write on CSV
		f = open(fname,"a",newline="")
		csv_writer = csv.writer(f)
		csv_writer.writerow([currentTime, round(H,3), round(T,3), round(bus_voltage,3), fanStatus, heatStatus])
		f.close()
		time.sleep(time_interval)


if __name__ == "__main__":
	main()
