import RPi.GPIO as GPIO
import datetime
import csv
import time
from ina219 import INA219, DeviceRangeError
from time import sleep
import Adafruit_DHT
import sys


#----------GPIO SETTINGS------------
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

#----------INA SETTING------------
SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 2.0
ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS)
ina.configure(ina.RANGE_16V)
currentDT = datetime.datetime.now()
'''
fan setting
#-----------FAN PIN SETTINGS------------
fanPIN = 4
GPIO.setup(fanPIN, GPIO.OUT)
'''
#-----------Global Var-------------------------
fanStatus =0
date = datetime.datetime.now()

#-----------File------------
fname = "Prototype"+ str(date.month) + str(date.day) + str(date.hour) + ".csv"
time_interval = 600

def difTime():
    sub = datetime.timedelta(1)
    return sub

def main():  
    f = open(fname,"w",newline="")
    csv_writer = csv.writer(f)
    csv_writer.writerow(['Time', 'Humidity', 'Temperature', 'Voltage'])
    f.close()
    V = 0
    
    while True:
        H, T = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302,'4')
        #RH, RT = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302,'12')
        #print(RH)
        bus_voltage = ina.voltage()
        now = str(datetime.datetime.now()-difTime())
        f = open(fname,"a",newline="")
        csv_writer = csv.writer(f)
        csv_writer.writerow([now, H, T,bus_voltage])
        f.close()
        time.sleep(time_interval)

if __name__ == "__main__":
    main()
