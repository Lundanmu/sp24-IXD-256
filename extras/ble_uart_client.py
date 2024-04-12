# BLE UART client example for M5Stack AtomS3
# run the BLE UART server example on another AtomS3 board

import os, sys, io
import M5
from M5 import *
from bleuart import *
import time

ble_client = None

def setup():
  global ble_client
  M5.begin()
  ble_client = BLEUARTClient()
  ble_client.connect('ble-uart', timeout=2000)
  print('connected =', ble_client.is_connected())
    
def loop():
  global ble_client
  M5.update()
  data = ble_client.read()
  if(data != ''):
    print('data =', data.decode())
  time.sleep_ms(100)
  
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

