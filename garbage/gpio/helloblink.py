#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

channel = 6

GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)

while True:
    GPIO.output(channel, 0)
    time.sleep(1)
    GPIO.output(channel, 1)
    time.sleep(1)
