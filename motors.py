import RPi.GPIO as GPIO
import yaml
from time import sleep

with open("config/config.yml", "r") as f:
	configs = f.load()

class move(object):
	
	
	def __init__(self):
                GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		# self.dir_ud = configs["gpio"]["dir_ud"]
                direction = 23
                step = 25
		GPIO.setup(direction, GPIO.OUT)
		GPIO.setup(step, GPIO.OUT)
		GPIO.setup(21, GPIO.IN)
		#waitTime = .01  #stepper speed (.01 works with stepper and driver without missing steps)

        def UD_Home(self):
		# get rid of these definitions here and refernece via self.dir_ud        
                direction = 23
                step = 25
                udPin = 21
                waitTime = .001
                
		GPIO.setup(direction, GPIO.OUT)
		GPIO.setup(step, GPIO.OUT)
		GPIO.setup(udPin, GPIO.IN)
		
    		GPIO.output(direction, False)

                home = GPIO.input(udPin)
    		while home == 0:
                        GPIO.output(step, True)
                        GPIO.output(step, False)
                        sleep(waitTime)
                        home = GPIO.input(udPin)

        def LR_Home(self):        
                direction = 18
                step = 24
                lrPin = 20
                waitTime = .001
                
		GPIO.setup(direction, GPIO.OUT)
		GPIO.setup(step, GPIO.OUT)
		GPIO.setup(lrPin, GPIO.IN)
		
    		GPIO.output(direction, False)

                home = GPIO.input(lrPin)
    		while home == 0:
                        GPIO.output(step, True)
                        GPIO.output(step, False)
                        sleep(waitTime)
                        home = GPIO.input(lrPin)
	
	def tiltUP(self):
                direction = 23
                step = 25
                waitTime = .001 #.001 is the best
		GPIO.setup(direction, GPIO.OUT)
		GPIO.setup(step, GPIO.OUT)
    		GPIO.output(direction, True)
                stepCounter = 0

                while stepCounter < 50:
                        #turning on and off forces one step
                        GPIO.output(step, True)
                        GPIO.output(step, False)
                        stepCounter += 1
                        sleep(waitTime)

        
	def tiltDOWN(self):
                direction = 23
                step = 25
                waitTime = .001
		GPIO.setup(direction, GPIO.OUT)
		GPIO.setup(step, GPIO.OUT)
    		GPIO.output(direction, False)
                stepCounter = 0

                while stepCounter < 50:
                        #turning on and off forces one step
                        GPIO.output(step, True)
                        GPIO.output(step, False)
                        stepCounter += 1
                        sleep(waitTime)

	def panLEFT(self):
                direction = 18
                step = 24
                waitTime = .001 #.001 is the best
		GPIO.setup(direction, GPIO.OUT)
		GPIO.setup(step, GPIO.OUT)
    		GPIO.output(direction, True)
                stepCounter = 0

                while stepCounter < 50:
                        #turning on and off forces one step
                        GPIO.output(step, True)
                        GPIO.output(step, False)
                        stepCounter += 1
                        sleep(waitTime)

	def panRIGHT(self):
                direction = 18
                step = 24
                waitTime = .001 #.001 is the best
		GPIO.setup(direction, GPIO.OUT)
		GPIO.setup(step, GPIO.OUT)
    		GPIO.output(direction, True)
                stepCounter = 0

                while stepCounter < 50:
                        #turning on and off forces one step
                        GPIO.output(step, True)
                        GPIO.output(step, False)
                        stepCounter += 1
                        sleep(waitTime)
                        
GPIO.cleanup()
