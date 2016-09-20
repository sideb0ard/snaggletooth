#!/usr/bin/env python

import sys
import os 
import time

pin0 = 4
pin1 = 27
pwmDev = open('/dev/pi-blaster', 'w')

def pwm_range(start, end, step):
  while start <= end:
    yield start
    start += step

def fade_up(pin):
  for i in pwm_range(0, 1, .01):
    pwmDev.write('%d=%s\n'%(pin, str(i)))
    time.sleep(.01)

fade_up(pin0)
fade_up(pin1)
