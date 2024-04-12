# BLE UART server example for M5Stack AtomS3
# run the BLE UART client example on another AtomS3 board

import os, sys, io
import M5
from M5 import *
from bleuart import *
import time

ble_server = None

def setup():
  global ble_server
  M5.begin()
  ble_server = BLEUARTServer(name='ble-uart')

def loop():
  global ble_server
  M5.update()
  print('write to bleuart..')
  ble_server.write('hello M5!')
  time.sleep_ms(2000)
  
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
