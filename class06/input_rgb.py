# using the input function for receiving r,g,b values

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

title0 = None
label0 = None
rgb = None
r = 0
r_final = 0

def setup():
  global title0, label0, rgb
  M5.begin()
  # display title ("title text", text offset, fg color, bg color, font):
  title0 = Widgets.Title("TITLE", 3, 0x000000, 0xffffff, Widgets.FONTS.DejaVu18)
  # display label ("label text", x, y, layer number, fg color, bg color, font):
  label0 = Widgets.Label("label", 3, 20, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  # initialize RGB LED strip on pin 38 with 30 pixels:
  rgb = RGB(io=38, n=30, type="SK6812")

def get_color(r, g, b):
  rgb_color = (r << 16) | (g << 8) | b
  return rgb_color

def loop():
  global rgb
  global r, r_final
  M5.update()
  if r == r_final:
    input_str = input('input red value: ')
    print('received:', input_str)
    r_final = int(input_str)
  else:
    if r < r_final:
      r += 1
    elif r > r_final:
      r -= 1
    c = get_color(r, 0, 0)
    rgb.fill_color(c)
  
  time.sleep_ms(5)
  
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