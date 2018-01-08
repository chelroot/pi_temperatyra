#! /usr/bin/env python
# coding: utf-8

import RPi.GPIO as GPIO
import time, os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)

while True :
 GPIO.output(21,True),
 time.sleep(0.5)
 GPIO.output(21,False),
 time.sleep(1)

