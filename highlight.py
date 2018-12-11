import RPi.GPIO as GPIO
import time

RED_PIN = 20
UV_PIN = 16
ECHO_PIN = 21
TRIG_PIN = 19


class PiThing(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RED_PIN,GPIO.OUT) # LED output
        GPIO.setup(UV_PIN,GPIO.OUT)
        GPIO.setup(ECHO_PIN,GPIO.IN) # Echo input
        GPIO.setup(TRIG_PIN,GPIO.OUT) # Trigger output

    def ultrasound(self):
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(ECHO_PIN,GPIO.IN) # Echo input
        #GPIO.setup(TRIG_PIN,GPIO.OUT) # Trigger output
        print("Distance Measurement in Progress")
        GPIO.output(TRIG_PIN,False)
        print("Waiting for Sensor to Settle")
        time.sleep(2)
        print("Sleep")
        GPIO.output(TRIG_PIN,True)
        print("TRIG")
        time.sleep(0.00001)
        print("0.0001")
        GPIO.output(TRIG_PIN,False)

        while GPIO.input(ECHO_PIN) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO_PIN) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance,2)
        print "Distance:",distance,2,"cm"

        return distance

    def setRedLED(self,value):
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(RED_PIN,GPIO.OUT) # LED output
        GPIO.output(RED_PIN,value)

    def setUVLED(self,value):
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(UV_PIN,GPIO.OUT)
        GPIO.output(UV_PIN,value)
