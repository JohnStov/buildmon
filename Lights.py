import RPi.GPIO as GPIO
import time

# we have to use BCM mode to stay compatible with the dot3k
GPIO.setmode(GPIO.BCM)

lamps = [6, 13, 19, 26]
for lamp in lamps:
    GPIO.setup(lamp, GPIO.OUT)

def set_lamp(lamp_id, state):
    if lamp_id >= 0 and lamp_id < len(lamps):
        GPIO.output(lamps[lamp_id], state)
    
def all_off():
    for lamp in range(0, len(lamps)):
        set_lamp(lamp, 0)

def build_good():
    set_lamp(0, 1)
    set_lamp(1, 1)
    set_lamp(2, 0)
    set_lamp(3, 0)

def broken_test():
    set_lamp(0, 0)
    set_lamp(1, 1)
    set_lamp(2, 0)
    set_lamp(3, 0)

def broken_build():
    set_lamp(0, 0)
    set_lamp(1, 0)
    set_lamp(2, 1)
    set_lamp(3, 0)

all_off()
