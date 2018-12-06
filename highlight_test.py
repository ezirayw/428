from highlight import PiThing
import time


pi_thing =  PiThing()

print('Blinking LED (Ctrl+C to stop)')
while True:
    pi_thing=setLED(True)
    time.sleep(0.5)
    pi_thing=setLED(False)
    time.sleep(0.5)
