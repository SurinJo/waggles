import RPI.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

battery = 4
cooling = 17
heating = 27


GPIO.setup(battery,GPIO.OUT)
GPIO.setup(cooling,GPIO.OUT)
GPIO.setup(heating,GPIO.OUT)

#pinState = [1,1,1] #0 = HIGH, 1 =LOW
pinState = {'battery':1, 'fan':1, 'heat':1}
def changePin(key):
	pinState =  {
		0 : pinState['battery'] = -pinState['battery']
		#1 : pinState[1] = -pinState[1],
		#2 : pinState[2] = -pinState[2]
	}
	return switcher.get(input, "wrong number")

def changePinState:
	if pinState[0] == 0:
		GPIO.output(battery,GPIO.HIGH)
	else:
		GPIO.output(battery,GPIO.LOW)

	if pinState[1] == 0:
		GPIO.output(cooling, GPIO.HIGH)
	else:
		GPIO.output(cooling ,GPIO.LOW)
	if pinState[2] ==0:
		GPIO.output(heating, GPIO.HIGH)
	else :
		GPIO.output(heating, GPIO.LOW)

def main
	while 1:
		key = int(input('open module number:'))
		changePin(key)
		changePinState()

if __name__ == "__main__"
	main()
