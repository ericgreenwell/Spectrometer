import sys
import RPi.GPIO as gpio
import time

#read arguments
try:
        direction = sys.argv[1]
        steps = int(float(sys.argv[2]))
except:
        steps = 0

# print which direction and how many steps
print('you said turn %s %s steps.') % (direction,steps)


#setup GPIO using broadcom layout BCM
gpio.setmode(gpio.BCM)
#GPIO23 = Direction
#GPIO24 = Step
gpio.setup(23, gpio.OUT)
gpio.setup(25, gpio.OUT)

# set rotation and direction (true = left false = right)

if direction == 'left':
	gpio.output(23, True)
elif direction == 'right':
	gpio.output(23, False)

stepCounter = 0

#waittime controls speed .001 is sufficiently fast and quiet
#POT voltage of .5V is quiet with the NEMA 17 steppers and new stepper drivers

waitTime = .001


while stepCounter < steps:
	#turning on and off tells to make a step
	gpio.output(25,True)
	gpio.output(25,False)
	stepCounter += 1

	time.sleep(waitTime)

#clear GPIOs
gpio.cleanup()

