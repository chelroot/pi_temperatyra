#! /usr/bin/env python
# coding: utf-8

import RPi.GPIO as GPIO
import time
from datetime import datetime


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(19, GPIO.IN)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию

f1 = "/home/pi/a2.html"
a2 = open(f1, 'a')

now = datetime.now()

if (GPIO.input(19)) == 0:
    a2 = open(f1, 'a')
    a2.write('<br />' + '19' + '  on  ' + str(now) + '\n'),
    a2.close()

    print('19' + '   on  ' + str(now) + '\n'),

if (GPIO.input(19)) == 1:
    a2 = open(f1, 'a')
    a2.write('<br />' + '19' + '  off ' + str(now) + '\n'),
    a2.close()

    print('19' + '   off ' + str(now) + '\n'),



