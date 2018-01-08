#! /usr/bin/env python
# coding: utf-8

import RPi.GPIO as GPIO
import time, os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)

GPIO.output(21,False),
print('21' + '  off ')

