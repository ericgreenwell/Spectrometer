#!usr/bin/env python

import serial
from RPI.GPIO import GPIO
import matplotlib.pyplot as plt

SPEC_TRG   =      5
SPEC_ST    =      6
SPEC_CLK   =      13
SPEC_VIDEO =      19
WHITE_LED  =      26
LASER_404  =      22

#SPI Configuration
"""
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

USE:
values[i] = mcp.read_adc(i)

"""



"""
sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus git
cd ~
git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git
cd Adafruit_Python_MCP3008
sudo python setup.py install
"""

SPEC_CHANNELS = 288

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
  data = []
  for i in range(SPEC_CHANNELS):
          data[i] = mcp.read_adc(1) # analog read a channel 1 of ADC
          
          GPIO.output(SPEC_CLK, GPIO.HIGH)
          time.sleep(delayTime)
          GPIO.output(SPEC_CLK, GPIO.LOW)
          time.sleep(delayTime)
  
  GPIO.output(SPEC_CLK, GPIO.HIGH)
  time.sleep(delayTime)
       
  
  # Print Data
  
  # Plot Data
  def plot:
    plt.plot(data)
    plt.ylabel('Intensity')
    plt.xlabel('Wavelength')
    plt.show()
  
  
  
  if __name__ == "__main__":
    readSpectrometer()
    plot()
        
        
        
        
