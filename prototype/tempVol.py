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
time_interval = 1

def difTime():
    sub = datetime.timedelta(1)
    return sub

def main():  
    f = open(fname,"w",newline="")
    csv_writer = csv.writer(f)
    csv_writer.writerow(['Time', 'Humidity', 'Temperature', 'Voltage','Current','Power'])
    f.close()
    V = 0
    work_time =0;
    while True:
        H, T = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302,'4')
        bus_voltage = ina.voltage()
        bus_current = ina.current()
        bus_power = ina.power()
        work_time = work_time + time_interval/60
        f = open(fname,"a",newline="")
        csv_writer = csv.writer(f)
        csv_writer.writerow([round(work_time,2), round(float(H),2), round(float(T),2),round(float(bus_voltage),2),round(float(bus_current),2),bus_power])
        f.close()
        time.sleep(time_interval)

if __name__ == "__main__":
    main()
