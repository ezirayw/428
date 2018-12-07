from highlight import PiThing
import time


pi_thing =  PiThing()

print('Blinking LED (Ctrl+C to stop)')
while True:
    pi_thing.setREDLED(True)
    pi_thing.setUVLED(True)
    time.sleep(0.5)
    pi_thing.setREDLED(False)
    pi_thing.setUVLED(False)
    time.sleep(0.5)
