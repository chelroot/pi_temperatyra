#! /usr/bin/env python
# coding: utf-8

import RPi.GPIO as GPIO
import time, os

LATCH = 19 # Pin  Latch clock
CLK = 13 # Pin  shift clock
dataBit = 26 # Pin  A

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup(LATCH, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(dataBit, GPIO.OUT)


GPIO.output(LATCH, 0)
GPIO.output(CLK, 0)


def pulseCLK():
    GPIO.output(CLK, 1)
   # time.sleep(.01)
    GPIO.output(CLK, 0)
    return

def serLatch():
    GPIO.output(LATCH, 1)
   # time.sleep(.01)
    GPIO.output(LATCH, 0)
    return

# MSB out first!
def sW(value):
    for  x in range(0,8):
        temp = value & 0x80
        if temp == 0x80:
           GPIO.output(dataBit, 1) # data bit HIGH
        else:
           GPIO.output(dataBit, 0) # data bit LOW
        pulseCLK()
        value = value << 0x01 # shift left
    serLatch() # output byte
    return


# convert an 8-bit number to a binary string
def convBinary(value):
    binaryValue = '0b'
    for  x in range(0,8):
        temp = value & 0x80
        if temp == 0x80:
           binaryValue = binaryValue + '1'
        else:
            binaryValue = binaryValue + '0'
        value = value << 1
    return binaryValue

t=2
a1=1; a2=2; a3=4; a4=8; a5=16; a6=32; a7=64; a8=128

aa = a1 + a2 + a3 + a4 + a5 +a6 + a7 + a8
aa1 = 255 - a3 - a5
print(aa)

print(aa1)
v1=254; v2=253; v3=251; v4=247; v5=239; v6=223; v7=191; v8=127

vv=255
v0=0
v37=195
va=15


while True :
#сдвиг по одному
  sW(a1 + a2 + a4 + +a6 + a7 + a8)
  time.sleep(t)
  sW(vv)
  time.sleep(t)

