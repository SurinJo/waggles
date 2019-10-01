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
cmd = 'temp'
seri = serial.Serial(port, baudrate = brate, timeout = None)


#-----------File------------
fname = "solarWithFanPrototype.csv"
time_interval = 10

def difTime():
    sub = datetime.timedelta(1)
    return sub

def main():  
    f = open(fname,"w",newline="")
    csv_writer = csv.writer(f)
    csv_writer.writerow(['Time', 'Humidity', 'Temperature', 'Voltage'])
    f.close()

    while true:
        H, T = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302,'17')
        
        if seri.in_waiting != 0:
            content = seri.readline()
            V = content[:-2].decode()
    
        key = input()
        if(key == 0):
            GPIO.output(pin, GPIO.LOW)
        elif(key == 1):
            GPIO.output(pin, GPIO.HIGH)
        elif(key == 2):
            sys.exit()
        else:
            print("Wrong Input")

        now = str(datetime.datetime.now()-difTime())
        f = open(fname,"a",newline="")
        csv_writer = csv.writer(f)
        csv_writer.writerow([now, H, T, V])
        f.close()
        time.sleep(time_interval)

if __name__ == "__main__":
    main()