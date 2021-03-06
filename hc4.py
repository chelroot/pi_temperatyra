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
def ssrWrite(value):
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


def ssrWrite1(value):
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

t=1
tt=2

while True :
 #мигаем 1
  #сдвиг по одному
  # Все одновременно
 ssrWrite(255)
 ssrWrite1(255)
 time.sleep(tt)
 ssrWrite(0)
 ssrWrite1(0)
 time.sleep(tt)
 ssrWrite(255)
 ssrWrite1(255)
 time.sleep(tt)
 ssrWrite(0)
 ssrWrite1(0)
 ssrWrite(255)
 ssrWrite1(255)
 time.sleep(tt)
 ssrWrite(0)
 ssrWrite1(0)
 time.sleep(tt)
 ssrWrite(255)
 ssrWrite1(255)
 time.sleep(tt)
 ssrWrite(0)
 ssrWrite1(0)
