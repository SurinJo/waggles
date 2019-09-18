import RPi.GPIO as GPIO
import Adafruit_DHT
from ina219 import INA219, DeviceRangeError
import time
from time import sleep

#----------GPIO SETTINGS------------
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

#-----------PIN SETTINGS------------
batteryPin = 18
fanPin = 12
heatingPin = 21

pinList = [batteryPin, fanPin, heatingPin]

for i in pinList:
    GPIO.setup(i, GPIO.OUT)

#-----------ElECTRICAL VALUE, SENSOR SETTINGS------------
SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 2.0
ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS)
ina.configure(ina.RANGE_16V)

#-----------FUNCs_Relay------------
def setRelayByData(H, T):
    if(H > 70):
        GPIO.output(fanPin, GPIO.LOW)
    else:
        GPIO.output(fanPin, GPIO.HIGH)
    

#-----------FUNCs_Sensor------------
def getThermalSensorData():
    H, T = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302,'4')
    return H, T

def getCurrentSensorData():
    V = ina.voltage()
    I = ina.current()
    P = ina.power()
    return V, I, P

while True:
    H, T = getThermalSensorData()
    V, I, P = getCurrentSensorData()

    setRelayByData(H, T)
    print("Humidity: %f %%", H)
    print("Temperature: %f C", T)
    print("Bus Voltage: {0:0.4f} V".format(V))
    print("Bus Current: {0:0.2f} mA".format(I))
    print("Power: {0:0.2f} mW".format(P))
