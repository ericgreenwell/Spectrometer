#!usr/bin/env python

from flask import Flask, render_template, Response,flash,request, redirect, url_for, make_response
#import motors
import os
import serial
from threading import Lock
import mpld3
from mpld3 import plugins
#import RPi.GPIO as GPIO


app = Flask(__name__) #set up flask server
app.secret_key=os.urandom(24)
spec = serial.Serial('/dev/ttyUSB0',
              baudrate=115200,
              bytesize=serial.EIGHTBITS,
              timeout=0,
              stopbits=serial.STOPBITS_ONE,
              parity=serial.PARITY_NONE)
lock = Lock()
############# routes ############
@app.route('/')
def index():
        return render_template('index.html')

@app.route('/get_data')
def read_data():

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.title('Spectrometer Output')
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

        return data, mpld3.fig_to_html(fig)


#Uses methods from motors.py to send commands to the GPIO to operate the motors

#@app.route('/move/<direction>', methods =['POST'])
@app.route('/plot', methods=['POST'])
def plot():
    data = json.loads(request.data)
    return draw_figure(data)

############# utils ###########
def draw_figure(data):

    with lock:
        fig, ax = plt.subplots()
        ax.plot(data)

    return mpld3.fig_to_html(fig)


############# main ############
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True, threaded=True) #set up the server in debug mode to the port 5000

############# EOF ##############
