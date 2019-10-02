import RPi.GPIO as GPIO
import time

#----------GPIO SETTINGS------------
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

#-----------PIN # SETTINGS------------
batteryPIN = 4
fanPIN = 12
heatingPIN = 21

pinList = [batteryPIN, fanPIN, heatingPIN]

for i in pinList:
    GPIO.setup(i, GPIO.OUT)

def findKeyPin(key):
    return pinList[key]

def setByPin(pin, mode):
    if(mode == 0):
        GPIO.output(pin, GPIO.HIGH)
    elif(mode == 1):
        GPIO.output(pin, GPIO.LOW)
    else:
        print("Invalid mode input")


while 1:
    key = int(input("Input Number(0,1,2) : "))
    mode = int(input("Input Mode(0,1) : "))
    print("findKeyPin(key)v : ", findKeyPin(key))
    setByPin(findKeyPin(key),mode)

GPIO.cleanup()
