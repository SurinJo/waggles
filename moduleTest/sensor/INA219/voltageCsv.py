import datetime
import csv
import time
from ina219 import INA219, DeviceRangeError
import datetime
from time import sleep

#----------TIME Setting---------
date = datetime.datetime.now() # time variable for filename

#----------INA Setting-----------
SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 2.0
ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS)
ina.configure(ina.RANGE_16V)

#-----------GLOBAL Var----------
fname = "temp"+ str(date.month) + str(date.day) + str(date.hour) + ".csv"
time_interval = 10 * 60 
elapsed_time  = 0

def difTime():
    sub = datetime.timedelta(1)
    return sub

def main():  
    f = open(fname,"w",newline="")
    csv_writer = csv.writer(f)
    csv_writer.writerow(['time', 'bus_voltage'])
    f.close()

    while 1:
        bus_voltage = ina.voltage()
        elapsed_time =  elapsed_time + time_interval
        f = open(fname,"a",newline="")
        csv_writer = csv.writer(f)
        csv_writer.writerow([str(elapsed_time), bus_voltage])
        f.close()
        time.sleep(time_interval)

if __name__ == "__main__":
    main()
