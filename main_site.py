#!/usr/bin/env python3
from importlib import import_module
import os
from flask import Flask, render_template, Response
# check if root
if os.getuid() != 0:
    print("I can't run as a mortal. Sorry. Try to run me with admin privileges")
    exit()
# import camera driver

Camera = import_module('camera_opencv').Camera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')



def genTxt(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()[0]

        # print frame
        yield (str(frame))
        # yield (b'--frame\r\n'b'Content-Type: text/xml; charset=utf-8\r\n\r\n' + str(frame[0]) + b'\r\n')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        x = (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame[1] + b'\r\n')
        # print frame
        yield x
        # yield (b'--frame\r\n'b'Content-Type: text/xml; charset=utf-8\r\n\r\n' + str(frame[0]) + b'\r\n')


@app.route('/video_feed')
def video_feed():

    # print len(gen(Camera()))
    x = gen(Camera())
    # print frame
    # x = (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    return Response(x,
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/textdata')
def textdata():
    return  Response(genTxt(Camera()),
                    mimetype='text/csv')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)
