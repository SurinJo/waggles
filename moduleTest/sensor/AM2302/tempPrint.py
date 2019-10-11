import RPi.GPIO as GPIO
import Adafruit_DHT
import csv
import time
import datetime
from socket import gethostname

def get_sensor_data():
    H, T = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302,'4')
    return str(H), str(T)

def inditime():
    sub = datetime.timedelta(hours=5)
    return sub

def make_filename():
    filename = gethostname() + "_TH_"+str((datetime.datetime.now()-inditime()).strftime('%m%d_%H%M'))
    filename+='.csv'
    return filename

def main():

    while True:
        H,T = get_sensor_data()
        print(1)
        now = str(datetime.datetime.now()-inditime())
        print(2)
        print("Temp" , T , "Humidity", H, '\n')
        time.sleep(1)
if __name__ == "__main__":
    main()
