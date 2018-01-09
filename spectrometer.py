#!usr/bin/env python

import serial
from RPI.GPIO import GPIO

SPEC_TRG   =      5
SPEC_ST    =      6
SPEC_CLK   =      13
SPEC_VIDEO =      19
WHITE_LED  =      26
LASER_404  =      22

GPIO.setmode(GPIO.BCM)

GPIO.setup(SPEC_ST, GPIO.OUT)
GPIO.setup(SPEC_CLK, GPIO.OUT)
GPIO.setup(LASER_404, GPIO.OUT)
GPIO.setup(WHITE_LED, GPIO.OUT)

GPIO.setup(SPEC_VIDEO, GPIO.IN)
GPIO.setup(SPEC_TRG, GPIO.IN)

#serial begin

def readSpectrometer():
  delayTime = .000001
  
  GPIO.output(SPEC_CLK, GPIO.LOW)
  time.sleep(delayTime)
  GPIO.output(SPEC_CLK, GPIO.HIGH)
  time.sleep(delayTime)
  GPIO.output(SPEC_CLK, GPIO.LOW)
  GPIO.output(SPEC_ST, GPIO.HIGH)
  time.sleep(delayTime)
  
  for i in range(15):
        GPIO.output(SPEC_CLK, GPIO.HIGH)
        time.sleep(delayTime)
        GPIO.output(SPEC_CLK, GPIO.LOW)
        time.sleep(delayTime)
        
  # Set SPEC_ST LOW
  GPIO.output(SPEC_ST, GPIO.LOW)
  
  #Sample for a period of time
  for i in range(85):
        GPIO.output(SPEC_CLK, GPIO.HIGH)
        time.sleep(delayTime)
        GPIO.output(SPEC_CLK, GPIO.LOW)
        time.sleep(delayTime)
  
  GPIO.output(SPEC_CLK, GPIO.HIGH)
  time.sleep(delayTime)
  GPIO.output(SPEC_CLK, GPIO.LOW)
  time.sleep(delayTime)
  
  
  # Read from SPEC Video
  
  for i in range(SPEC_CHANNELS):
          data[i] = # analog read a channel
          
          GPIO.output(SPEC_CLK, GPIO.HIGH)
          time.sleep(delayTime)
          GPIO.output(SPEC_CLK, GPIO.LOW)
          time.sleep(delayTime)
  
  GPIO.output(SPEC_CLK, GPIO.HIGH)
  time.sleep(delayTime)
       
  
  # Print Data
  
        
        
        
        
