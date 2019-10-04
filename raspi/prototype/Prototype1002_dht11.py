import RPi.GPIO as GPIO
import datetime
import csv
import time
from ina219 import INA219, DeviceRangeError
from time import sleep
import Adafruit_DHT
import sys
import serial


#----------GPIO SETTINGS------------
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()


#-----------FAN PIN SETTINGS------------
fanPIN = 4
GPIO.setup(fanPIN, GPIO.OUT)


#-----------VOLTAGE SENSOR SETTINGS-------------
port = '/dev/ttyACM0'
brate = 9600 #boudrate
seri = serial.Serial(port, baudrate = brate, timeout = None)

#-----------Global Var-------------------------
fanStatus =0
date = datetime.datetime.now()
#-----------File------------

fname = "solarWithFanPrototype"+ str(date.month) + str(date.day) + str(date.hour) + ".csv"
time_interval = 600

def difTime():
    sub = datetime.timedelta(1)
    return sub

def main():  
    f = open(fname,"w",newline="")
    csv_writer = csv.writer(f)
    csv_writer.writerow(['Time', 'Humidity', 'Temperature', 'Voltage', 'FanStatus'])
    f.close()
    V = 0
    H= 0 
    T = 0  
    while True:
        if seri.in_waiting != 0:
            content = seri.readline()
            dataMon = content[:-2].decode()

            dataList = dataMon.split(',')
            #print(dataList)
            if len(dataList)==3:
                T = dataList[0]
                H = dataList[1]
                V = dataList[2]
            

        else:
            print("Can't get serial")
        
        
        GPIO.output(fanPIN, GPIO.LOW)
        time.sleep(time_interval)
        
        now = str(datetime.datetime.now()-difTime())
        f = open(fname,"a",newline="")
        csv_writer = csv.writer(f)
        csv_writer.writerow([now, H, T, V, fanStatus])
        f.close()

        time.sleep(time_interval)
if __name__ == "__main__":
    main()
