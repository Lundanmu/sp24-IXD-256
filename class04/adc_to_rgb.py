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
rgb = None

def setup():
  global label0, adc1
  M5.begin()
  # initialize dispaly title and label:
  title0 = Widgets.Title("ADC test", 3, 0x000000, 0xffffff, Widgets.FONTS.DejaVu18)
  label0 = Widgets.Label("--", 3, 20, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  # initialize analog to digital converter on pin 1:
  adc1 = ADC(Pin(1), atten=ADC.ATTN_11DB)
  # initialize RGB LED strip on pin 38 with 10 pixels:
  rgb = RGB(io=38, n=10, type="SK6812")
  # fill RGB LEDs with green:
  #rgb.fill_color(0x003300)
  # fill RGB LEDs with orange:
  rgb.fill_color(get_color(255, 60, 0))
  
def get_color(r, g, b):
  rgb_color = (r << 16) | (g << 8) | b
  return rgb_color

# function to map input value range to output value range:
def map_value(in_val, in_min, in_max, out_min, out_max):
  out_val = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
  if out_val < out_min:
    out_val = out_min
  elif out_val > out_max:
    out_val = out_max
  return int(out_val)

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

