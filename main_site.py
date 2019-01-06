#!/usr/bin/env python3
from importlib import import_module
import os
from flask import Flask, render_template, Response
# check if root
if os.getuid() != 0:
    print("I can't run as a mortal. Sorry. Try to run me with admin privileges")
    exit()

Camera = import_module('camera_opencv_process').Camera

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    x = gen(Camera())
    return Response(x,
                    mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)
