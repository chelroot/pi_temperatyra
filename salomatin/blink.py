#! /usr/bin/env python
# coding: utf-8

import RPi.GPIO as GPIO
import time, os

aa = 11
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(aa, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

GPIO.output(2,False),
GPIO.output(3,False),
GPIO.output(7,False),

while True :
 GPIO.output(aa,True),
 time.sleep(0.5)
 GPIO.output(aa,False),
 time.sleep(1)

