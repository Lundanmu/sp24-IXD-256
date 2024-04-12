# test example for M5Stack HEART Unit (https://docs.m5stack.com/en/unit/heart)
# NOTE: the following max30100.py file should be saved to hardware:
# https://github.com/rafaelaroca/max30100/blob/master/max30100.py

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

from machine import Pin
from machine import I2C
import max30100  # import max30100.py

i2c = None
heart_sensor = None

def setup():
  global i2c, heart_sensor
  M5.begin()
  i2c = I2C(0, scl=Pin(39), sda=Pin(38)) #, freq=100000)
  print('Scanning I2C devices...')
  print(i2c.scan())
  heart_sensor = max30100.MAX30100(i2c=i2c)
  print('Reading MAX30100 registers...')
  print(heart_sensor.get_registers())
  heart_sensor.enable_spo2()
  print('finished setup..')


def loop():
  global i2c0, heart_sensor
  M5.update()
  heart_sensor.read_sensor()
  print(heart_sensor.ir, heart_sensor.red)
  time.sleep(0.5)
  


if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")

