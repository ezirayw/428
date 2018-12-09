from highlight import PiThing
import time


pi_thing =  PiThing()

print('Blinking LED (Ctrl+C to stop)')
while True:
    pi_thing.setRedLED(False)
    pi_thing.setUVLED(False)
