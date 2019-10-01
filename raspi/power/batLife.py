import datetime
import csv
import time
from time import sleep

#----------ina setting-----------
currentDT = datetime.datetime.now()

#---------------------
fname = "batteryLifeMeasure.csv"
time_interval = 5 * 60

def difTime():
    sub = datetime.timedelta(1)
    return sub

def main():  
    f = open(fname,"w",newline="")
    csv_writer = csv.writer(f)
    csv_writer.writerow(['time'])
    f.close()

    while 1:
        now = str(datetime.datetime.now()-difTime())
        f = open(fname,"a",newline="")
        csv_writer = csv.writer(f)
        csv_writer.writerow([now])
        f.close()
        time.sleep(time_interval)

if __name__ == "__main__":
    main()
