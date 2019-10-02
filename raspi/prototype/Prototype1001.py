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
#-----------File------------
fname = "solarWithFanPrototype.csv"
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

    while True:
        H, T = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302,'17')
        
        if seri.in_waiting != 0:
            content = seri.readline()
            #print(content[:-2].decode())
            V = content[:-2].decode()
        else:
            print("Can't get serial")
        
        
        GPIO.output(fanPIN, GPIO.LOW)
        
#----------Fan control--------
        if(T <= 30):
            GPIO.output(fanPIN, GPIO.LOW)
            fanStatus = 0
        else:
            GPIO.output(fanPIN, GPIO.HIGH)
            fanStatus = 1
#-----------------------------

        now = str(datetime.datetime.now()-difTime())
        f = open(fname,"a",newline="")
        csv_writer = csv.writer(f)
        csv_writer.writerow([now, H, T, V, fanStatus])
        f.close()
        time.sleep(time_interval)

if __name__ == "__main__":
    main()
