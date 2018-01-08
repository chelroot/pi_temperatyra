#! /usr/bin/env python
# coding: utf-8

import RPi.GPIO as GPIO
import time, os



import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO.setup(LED, GPIO.OUT)
GPIO.setup(21, GPIO.IN)
#GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   # подтяжка к земле

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию


pinstate = GPIO.input(21)




