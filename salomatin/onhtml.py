#! /usr/bin/env python
# coding: utf-8

import RPi.GPIO as GPIO
import time, os
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)

GPIO.output(21,True),
print('21' + '  on ')

f1 = "/home/pi/a2.html"
a2 = open(f1, 'a')

now = datetime.now()

a2 = open(f1, 'a')
a2.write('<br />' + '21' + '  on  ' + str(now) + '\n'),
a2.close()
