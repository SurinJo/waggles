import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import csv
import datetime
from ina219 import INA219, DeviceRangeError

SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 2.0
ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS)
ina.configure(ina.RANGE_16V)
currentDT = datetime.datetime.now()

