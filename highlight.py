import RPi.GPIO as GPIO
import time

LED_PIN = 20
ECHO_PIN = 21
TRIG_PIN = 26


class PiThing(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN,GPIO.OUT) # LED output
        GPIO.setup(ECHO_PIN,GPIO.IN) # Echo input
        GPIO.setup(TRIG_PIN,GPIO.OUT) # Trigger output

    def ultrasound(self):
        print("Distance Measurement in Progress")
        GPIO.output(TRIG,False)
        print("Waiting for Sensor to Settle")
        time.sleep(2)
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance,2)
        print "Distance:",distance,2,"cm"
        GPIO.cleanup()

        return distance

    def setLED(self,value):
        GPIO.output(LED_PIN,value)
