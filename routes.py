#!usr/bin/env python

from flask import Flask, render_template, json, request
import numpy as np
import serial
import time

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


############### Flags #################
status = 0



############# functions ############

def draw_fig(data):
    print 'drawing'
    fig, ax = plt.subplots()
    ax.plot(data)

    return mpld3.fig_to_html(fig)


app = Flask(__name__)

#################### Routes ###################

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/query', methods=['POST'])
def query():

    while True:

        spec.flush()
        line = spec.readline()

        if len(line) > 0:

            line = line.split(',')
            line = list(line)

            del line[-1]

            data = [int(x) for _, x in enumerate(line)]

            if len(data) == 288:
                return draw_fig(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
############# EOF ##############
