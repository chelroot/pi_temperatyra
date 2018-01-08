#! /usr/bin/env python
# coding: utf-8

import RPi.GPIO as GPIO
import time, os


LATCH = 2 # Pin  Latch clock
CLK = 3 # Pin  shift clock
dataBit = 5 # Pin  A
dataBit1= 6


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup(LATCH, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(dataBit, GPIO.OUT)
GPIO.setup(dataBit1, GPIO.OUT)


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


def sW1(value):
    for  x in range(0,8):
        temp = value & 0x80
        if temp == 0x80:
           GPIO.output(dataBit1, 1) # data bit HIGH
        else:
           GPIO.output(dataBit1, 0) # data bit LOW
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



t=0.5
tt=1
a1=1; a2=2; a3=4; a4=8; a5=16; a6=32; a7=64; a8=128
a34=12; a56=48; a78=192; a25=18; a246=44

v1=254; v2=253; v3=251; v4=247; v5=239; v6=223; v7=191; v8=127
vv=0
v0=255

sp1 = [a1, a2, a3, a34, a4, a56, a5, a78, a6, a246,  a7, a8, ] #vv, v0, ]
sp2 = [a1, a2, a3, a4, a5, a6, ] # vv, v0, ]


#sp1 = [v1, v2, v3, v4, v5, v6, v7, v8, ] #vv, v0, ]
#sp2 = [v1, v2, v3, v4, v5, v6, ] # vv, v0, ]
while True :
   for ii in sp1 :             # простая итерация списка
      sW(ii)
      time.sleep(t)
   for ii in sp2 :             # простая итерация списка
      sW1(ii)
      time.sleep(t)
   sW(255)
   time.sleep(tt)
   sW(0)
   time.sleep(tt)
   sW1(0)
   time.sleep(tt)
   sW(255)
   time.sleep(tt)
   sW(0)
   time.sleep(tt)
   sW1(0)
   time.sleep(tt)
   sW(255)
   time.sleep(tt)
   sW(0)
   time.sleep(tt)
   sW1(0)
   time.sleep(tt)
   sW(255)
   time.sleep(tt)
   sW(0)
   time.sleep(tt)
   sW1(0)
   time.sleep(tt)
   sW(255)
   time.sleep(tt)
   sW(0)
   time.sleep(tt)
   sW1(0)
   time.sleep(tt)
   sW(255)
   time.sleep(tt)
   time.sleep(tt)
   sW(0)
   time.sleep(tt)
   sW1(0)
   time.sleep(tt)
   sW(255)
   time.sleep(tt)
   sW(0)
   time.sleep(tt)
   sW1(0)
   time.sleep(tt)
   sW(255)
   time.sleep(tt)
   sW(0)
   time.sleep(tt)
   sW1(0)


   sW(255)
   time.sleep(tt)
   sW(0)
   time.sleep(tt)
   sW1(0)
   time.sleep(tt)
   sW(255)
   time.sleep(tt)
   sW(0)
   time.sleep(tt)
   sW1(0)
   time.sleep(tt)
   sW(255)
   time.sleep(tt)
   sW(0)
   time.sleep(tt)
   sW1(0)
   time.sleep(tt)
   sW(255)
   time.sleep(tt)
   sW(0)
   time.sleep(tt)
   sW1(0)
   time.sleep(tt)
   

   sW(255)
   time.sleep(tt)
   sW(0)
   time.sleep(tt)
   sW1(0)
   time.sleep(tt)
   sW(255)
   time.sleep(tt)
   sW(0)
   time.sleep(tt)
   sW1(0)
   time.sleep(tt)
   sW(255)
   time.sleep(tt)
   sW(0)
   time.sleep(tt)
   sW1(0)
   time.sleep(tt)
   sW(255)
   time.sleep(tt)
   sW(0)
   time.sleep(tt)
   sW1(0)
   time.sleep(tt)


# time.sleep(tt)

