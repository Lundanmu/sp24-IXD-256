# beginner program for M5Stack AtomS3 based on uiflow2 code structure

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

title0 = None
label0 = None

def setup():
  global title0, label0
  M5.begin()
  # display title ("title text", text offset, fg color, bg color, font):
  title0 = Widgets.Title("TITLE", 3, 0x000000, 0xffffff, Widgets.FONTS.DejaVu18)
  # display label ("label text", x, y, layer number, fg color, bg color, font):
  label0 = Widgets.Label("label", 3, 20, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  
def loop():
  M5.update()
  # wait for 100 milliseconds (1/10 second):
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
