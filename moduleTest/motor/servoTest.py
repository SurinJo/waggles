# Use Raspberry Pi to control Servo Motor motion
# Tutorial URL: http://osoyoo.com/?p=937

import RPi.GPIO as GPIO
import time
import os

GPIO.setwarnings(False)
# Set the layout for the pin declaration

# The Raspberry Pi pin 11(GPIO 18) connect to servo signal line(yellow wire)
# Pin 11 send PWM signal to control servo motion
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
#GPIO.setup(11, GPIO.OUT)

# menu info
print "l = move to the left"
print "r = move to the right"
print "m = move to the middle"
print "t = test sequence"
print "q = stop and exit"
Servo = GPIO.PWM(7, 50) 
while True:
	# Now we will start with a PWM signal at 50Hz at pin 18. 
	# 50Hz should work for many servos very will. If not you can play with the frequency if you like.
	print("back to start")
	# This command sets the left position of the servo
	Servo.start(7.5)
        time.sleep(1)
        Servo.ChangeDutyCycle(12.5)
        time.sleep(1)
        Servo.ChangeDutyCycle(2.5)
        time.sleep(1)

        
	
