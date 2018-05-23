#!usr/bin/env python

from flask import Flask, render_template, Response,flash,request, redirect, url_for, make_response
#import motors
import os
import serial
import threading
#import RPi.GPIO as GPIO


app = Flask(__name__) #set up flask server
app.secret_key=os.urandom(24)
spec = serial.Serial('/dev/ttyUSB0',
              baudrate=115200,
              bytesize=serial.EIGHTBITS,
              timeout=0,
              stopbits=serial.STOPBITS_ONE,
              parity=serial.PARITY_NONE)

############# routes ############
@app.route('/')
def index():
        return render_template('index.html')

@app.route('/get_data')
def video_feed():
        return Response(gen(Camera()),
                        mimetype = 'multipart/x-mixed-replace; boundary=frame')

#Uses methods from motors.py to send commands to the GPIO to operate the motors

#@app.route('/move/<direction>', methods =['POST'])
@app.route('/plot', methods=['POST'])
def plot():
	      

############# utils ###########
def gen(camera):
        """video streaming function"""
        while True:
                frame = camera.get_frame()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                
############# main ############
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True, threaded=True) #set up the server in debug mode to the port 5000

############# EOF ##############
