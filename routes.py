#!usr/bin/env python

from flask import Flask, render_template, json, request
import numpy as np
import serial

import matplotlib
import json
import random

matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.ioff()

from threading import Lock

lock = Lock()
import datetime
import mpld3
from mpld3 import plugins

spec = serial.Serial('/dev/ttyUSB0',
                     bytesize=serial.EIGHTBITS,
                     baudrate=115200,
                     timeout=0,
                     stopbits=serial.STOPBITS_ONE,
                     parity=serial.PARITY_NONE)

# Setting up matplotlib sytles using BMH
#s = json.load(open("./static/bmh_matplotlibrc.json"))
#matplotlib.rcParams.update(s)



############# routes ############

def draw_fig(data):
    with lock:
        fig, ax = plt.subplots()
        ax.plot(data)

        """elif fig_type == "area":
            ax.plot(x, y)
            ax.fill_between(x, 0, y, alpha=0.2)
        """
    return mpld3.fig_to_html(fig)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/query', methods=['POST'])
def query():
    spec.flush()
    line = spec.readline()
    print "in query"
    data = []

    if len(line) > 0:

        line = line.split(',')
        line = list(line)

        del line[-1]

        data = [int(x) for _, x in enumerate(line)]
        print len(data)

        if len(data) == 288:
            #fig, ax = plt.subplots()
            #ax.plot(data, 'r-')

            #ax = fig.add_subplot(1, 1, 1)
            #ax.title('Spectrometer Output')
            #ax.plot(data, 'r-')
            #fig.canvas.draw()
            #fig.canvas.flush_events()

            #return data

            return draw_fig(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
############# EOF ##############
