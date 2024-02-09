# ADC test example for M5Stack AtomS3

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

title0 = None
label0 = None
adc1 = None
adc1_val = None

def setup():
  global label0, adc1
  M5.begin()
  # initialize dispaly title and label:
  title0 = Widgets.Title("ADC test", 3, 0x000000, 0xffffff, Widgets.FONTS.DejaVu18)
  label0 = Widgets.Label("--", 3, 20, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  # initialize analog to digital converter on pin 1:
  adc1 = ADC(Pin(1), atten=ADC.ATTN_11DB)

def loop():
  global label0, adc1, adc1_value
  M5.update()
  # read ADC value:
  adc1_val = adc1.read()
  # print the ADC value:
  print(adc1_val)
  # show ADC value on display label:
  label0.setText(str(adc1_val))
  time.sleep_ms(500)

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
