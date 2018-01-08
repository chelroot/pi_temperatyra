#! /usr/bin/env python
# coding: utf-8

import RPi.GPIO as GPIO
import time
from datetime import datetime


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(19, GPIO.IN)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию


now = datetime.now()

if (GPIO.input(19)) == 0:
    print('19' + '   on  ' + str(now) + '\n'),

if (GPIO.input(19)) == 1:
    print('19' + '  off  ' + str(now) + '\n'),

