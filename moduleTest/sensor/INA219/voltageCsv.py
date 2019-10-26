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
fname = "voltageResult"+ str(date.month) + str(date.day) + str(date.hour) + ".csv"
time_interval = 10 * 60 
#time_interval = 1

def difTime():
    sub = datetime.timedelta(1)
    return sub

def main():  
    f = open(fname,"w",newline="")
    csv_writer = csv.writer(f)
    csv_writer.writerow(['time', 'bus_voltage','bus_current', 'bus_power'])
    f.close()
    elapsed_time  = 0
    
    while 1:
        bus_voltage = ina.voltage()
        bus_current = ina.current()
        bus_power = ina.power()
        elapsed_time =  elapsed_time + time_interval/60
        f = open(fname,"a",newline="")
        csv_writer = csv.writer(f)
        csv_writer.writerow([str(elapsed_time), bus_voltage, bus_current, bus_power])
        f.close()
        time.sleep(time_interval)

if __name__ == "__main__":
    main()
