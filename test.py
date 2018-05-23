import serial
import time
from matplotlib import pyplot as plt
import matplotlib.animation as animate
import numpy as np

""""
include exception for '' character in line read

"""

spec = serial.Serial('/dev/ttyUSB0', baudrate=115200, bytesize=serial.EIGHTBITS, timeout=0)
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(1,1,1)


while True:
    spec.flush()
    line = spec.readline()

    data = []

    if len(line) > 0:

        line = line.split(',')
        line = list(line)

        del line[-1]

        data = [int(x) for _, x in enumerate(line)]
        print len(data)

        if len(data) == 288:
            ax.plot(data, 'r-')

        fig.canvas.draw()
        fig.canvas.flush_events()


    ax.cla()
    #fig.clf()
