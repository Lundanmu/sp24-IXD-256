import os, sys, io
import M5
from M5 import *
from hardware import *
import time

label0 = None
input_pin = None
input_value = 0
input_timer = 0
program_state = 'START'

def setup():
  global label0, input_pin

  M5.begin()
  label0 = Widgets.Label("input", 5, 5, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu18)
  # initialize input on pin 41 (built-in button):
  input_pin = Pin(41, mode=Pin.IN)
  # initialize input on pin 8 with pull up:
  #input_pin = Pin(8, mode=Pin.IN, pull=Pin.PULL_UP)

def loop():
  global label0, pin1
  global input_value
  global input_timer
  M5.update()
  # check input every 500 ms (half second):
  if time.ticks_ms() > input_timer + 500:
    input_timer = time.ticks_ms()  # update button_timer
    input_value = input_pin.value()
    if input_value == 0:
      label0.setText('pin ON')
    else:
      label0.setText('pin OFF')
  
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

