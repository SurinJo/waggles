import datetime
import csv
import time
from ina219 import INA219, DeviceRangeError
from time import sleep

#----------ina setting-----------
SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 2.0
ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS)
ina.configure(ina.RANGE_16V)
currentDT = datetime.datetime.now()


#---------------------
fname = "windEnergyMonitor.csv"
time_interval = 5 * 60

def difTime():
    sub = datetime.timedelta(1)
    return sub

def main():  
    f = open(fname,"w",newline="")
    csv_writer = csv.writer(f)
    csv_writer.writerow(['time', 'bus_voltage'])
    f.close()

    while 1:
        #read_ina219()      
        bus_voltage = ina.voltage()
        now = str(datetime.datetime.now()-difTime())
        f = open(fname,"a",newline="")
        csv_writer = csv.writer(f)
        csv_writer.writerow([now, bus_voltage])
        #print(now)
        f.close()
        time.sleep(time_interval)

if __name__ == "__main__":
    main()
