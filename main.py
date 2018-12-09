from flask import Flask, render_template, request, redirect
from highlight import PiThing
import time
import RPi.GPIO as GPIO


app = Flask(__name__)
pi_thing = PiThing()

RED_PIN = 20
UV_PIN = 16
ECHO_PIN = 21
TRIG_PIN = 26

skin = "hello"
attachment = "hello"
color = "hello"
#hello

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN,GPIO.OUT) # LED output
GPIO.setup(UV_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN) # Echo input
GPIO.setup(TRIG_PIN,GPIO.OUT) # Trigger output
@app.route('/')
def index():
    pi_thing.setRedLED(True)
    return render_template('index.html')

@app.route('/index.html',methods = ['POST'])
def hello():
    skin = request.form["selectSkin"]
    attachment = request.form["selectAttachment"]
    color = request.form["selectWave"]
    return redirect('/')
if color == "Infrared":
    pi_thing.setRedLED(True)
if color == "UV":
    pi_thing.setUVLED(True)
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)
