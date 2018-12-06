from highligh import PiThing
import time


pi_thing =  PiThing()

switch = pi_thing.readSwitch()
print('Switch:{0}'.format(switch))

print('Blinking LED (Ctrl+C to stop)')
while True:
    pi_thing=setLED(True)
    time.sleep(0.5)
    pi_thing=setLED(False)
    time.sleep(0.5)
