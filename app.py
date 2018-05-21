#!usr/bin/env python

from flask import Flask, render_template, Response,flash,request, redirect, url_for, make_response
import motors
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) #set up GPIO
GPIO.setwarnings(False)

# Raspberry pi camera module (reqires picamera package)
from camera_pi import Camera

app = Flask(__name__) #set up flask server
app.secret_key=os.urandom(24)

motor = motors.move() #create motor object


############# routes ############
@app.route('/')
def index():
        return render_template('index.html')

@app.route('/video_feed')
def video_feed():
        return Response(gen(Camera()),
                        mimetype = 'multipart/x-mixed-replace; boundary=frame')

#Uses methods from motors.py to send commands to the GPIO to operate the motors
@app.route('/move/<direction>', methods =['POST'])
def moving(direction):
	      
        move = int(direction)
        if move == 1:
                motor.tiltUP()
        elif move == 2:
                motor.tiltDOWN()
        elif move == 3:
                motor.panLEFT()
        elif move == 4:
                motor.panRIGHT()
        elif move == 5:
                motor.UD_Home() 
                motor.LR_Home()
                
        else:
                return "false"
        
	return "success"

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
