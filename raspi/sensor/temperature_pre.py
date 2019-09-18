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
	temp_interval = 5 * 60
	fname = make_filename()
	f = open(fname,"w",newline="")
	csv_writer = csv.writer(f)
	csv_writer.writerow(['time', 'temperature','humidity'])
	f.close()
	while True:
		f = open(fname, "a", newline="")
		H,T = get_sensor_data()
		now = str(datetime.datetime.now()-inditime())
		csv_writer = csv.writer(f)
		csv_writer.writerow([now,T,H])
		f.close()
		time.sleep(temp_interval)
if __name__ == "__main__":
	main()
