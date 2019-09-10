import datetime
import csv
from ina219 import INA219, DeviceRangeError
from time import sleep

SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 2.0
ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS)
ina.configure(ina.RANGE_16V)
currentDT = datetime.datetime.now()
fname = "batteryMeasureTest.csv"

def read_ina219():
    try:
        print(str(currentDT))
        print('Bus Voltage: {0:0.2f}V'.format(ina.voltage()))
        print('Bus Current: {0:0.2f}mA'.format(ina.current()))
        print('Power: {0:0.2f}mW'.format(ina.power()))
        print('Shunt Voltage: {0:0.2f}mV\n'.format(ina.shunt_voltage()))
                          
        f = open(fname,"w",newline="")
        csv_writer = csv.writer(f)
        csv_writer.writerow(['bus_voltage', 'bus_current','power', 'shunt_voltage'])
        f.close()

    except DeviceRangeError as e:
        # Current out of device range with specified shunt resister
        print(e)

def main():  
    f = open(fname,"w",newline="")
    csv_writer = csv.writer(f)
    csv_writer.writerow(['bus_voltage', 'bus_current','power', 'shunt_voltage'])
    f.close()

    while 1:
        #read_ina219()      
        bus_voltage = ina.voltage()
        bus_current = ina.current()
        power = ina.power()
        shunt_voltage= ina.shunt_voltage()
    
        f = open(fname,"a",newline="")
        csv_writer = csv.writer(f)
        csv_writer.writerow([bus_voltage, bus_current, power, shunt_voltage])
        f.close()
        sleep(1800)



if __name__ == "__main__":
    main()
