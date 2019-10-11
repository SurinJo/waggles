import RPi.GPIO as GPIO
import Adafruit_DHT
import csv
import time
import datetime
date = datetime.datetime.now()
fname = "temp"+ str(date.month) + str(date.day) + str(date.hour) + ".csv"
time_interval = 600


def get_sensor_data():
    H, T = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302,'4')
    return str(H), str(T)

def defTime():
    sub = datetime.timedelta(hours=5)
    return sub

def main():
    f = open(fname,"w",newline="")
    csv_writer = csv.writer(f)
    csv_writer.writerow(['Time', 'Humidity', 'Temperature'])
    f.close()
    
    while True:
        H,T = get_sensor_data()
        now = str(datetime.datetime.now()-defTime())
        f = open(fname,"a",newline="")
        csv_writer = csv.writer(f)
        csv_writer.writerow([now, H, T])
        f.close()
        time.sleep(time_interval)
if __name__ == "__main__":
    main()
