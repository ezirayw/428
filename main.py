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
count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN,GPIO.OUT) # LED output
GPIO.setup(UV_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN) # Echo input
GPIO.setup(TRIG_PIN,GPIO.OUT) # Trigger output

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/therapy',methods = ['POST'])
def therapy():
    skin = request.form['selectSkin']
    attachment = request.form['selectAttachment']
    color = request.form['selectWave']
    size = request.form['selectSize']
    duration = float(size * 20)
    distance = pi_thing.ultrasound()

    if color == 'I':
        pi_thing.setUVLED(False)
        pi_thing.setRedLED(True)
    if color == 'U':
        pi_thing.setRedLED(False)
        pi_thing.setUVLED(True)

    while True:
        distance = pi_thing.ultrasound()
        if distance > 10:
            pi_thing.setUVLED(False)
            pi_thing.setRedLED(False)
            break
    return redirect('/')

@app.route('/sterilze',methods = ['POST'])
def sterilze():
    UVbutton = request.form['UVON']
    if UVbutton == 'UVON':
        pi_thing.setUVLED(True)
    elif UVbutton =='UVOFF':
        pi_thing.setUVLED(False)
    return redirect('/')
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)
