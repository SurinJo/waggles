import RPi.GPIO as GPIO
import Adafruit_DHT
import csv
import time
import datetime
from socket import gethostname


def get_sensor_data():
	H1, T1 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,'2')
	H2, T2 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,'23')
	return str(H1), str(T1), str(H2), str(T2)

def inditime():
	sub = datetime.timedelta(hours=5)
	return sub

def make_filename():
	filename = gethostname() + "_TH_"+str((datetime.datetime.now()-inditime()).strftime('%m%d_%H%M'))
	filename+='.csv'
	return filename
 
def main():
	fname = make_filename()
	f = open(fname,"w",newline="")
	csv_writer = csv.writer(f)
	csv_writer.writerow(['time', 'temperature1','humidity1', 'temperature2','humidity2'])
	f.close()
	while True:
		f = open(fname,"a",newline="")
		H1,T1,H2,T2 = get_sensor_data()
		csv_writer = csv.writer(f)
		now = str(datetime.datetime.now()-inditime())
		csv_writer.writerow([now,T1,H1,T2,H2])
		f.close()
		time.sleep(60*5)
if __name__ == "__main__":
	main()
