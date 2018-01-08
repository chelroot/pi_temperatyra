#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import glob
import time
from datetime import datetime, timedelta

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

a1 = '28-0115a81b7eff'
a2 = '28-0115c05990ff'
a3 = '28-03160346f8ff'
a4 = '28-0316034b20ff'
a5 = '28-0115b146f6ff'
a6 = '28-031603467bff'
a7 = '28-03160348e3ff'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c#, temp_f

device_file = ('/sys/bus/w1/devices/' + a1 + '/w1_slave')
c1 = round(read_temp(), 1)

device_file = ('/sys/bus/w1/devices/' + a2 + '/w1_slave')
c2 = round(read_temp(), 1)

device_file = ('/sys/bus/w1/devices/' + a3 + '/w1_slave')
c3 = round(read_temp(), 1)

device_file = ('/sys/bus/w1/devices/' + a4 + '/w1_slave')
c4 = round(read_temp(), 1)

device_file = ('/sys/bus/w1/devices/' + a5 + '/w1_slave')
c5 = round(read_temp(), 1)

device_file = ('/sys/bus/w1/devices/' + a6 + '/w1_slave')
c6 = round(read_temp(), 1)

device_file = ('/sys/bus/w1/devices/' + a7 + '/w1_slave')
c7 = round(read_temp(), 1)

print(str(c1) + ' ' + str(c2) + ' ' + str(c3) + ' ' + str(c4) + ' ' + str(c5) + ' ' + str(c6) + ' ' + str(c7))


ttt = datetime.now()
print(ttt)