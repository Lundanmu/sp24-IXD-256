# using the input function to change PWM duty cycle to control a servo

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

title0 = None
label0 = None
pwm1 = None

def setup():
  global title0, label0, pwm1
  M5.begin()
  # display title ("title text", text offset, fg color, bg color, font):
  title0 = Widgets.Title("PWM servo", 3, 0x000000, 0xffffff, Widgets.FONTS.DejaVu18)
  # display label ("label text", x, y, layer number, fg color, bg color, font):
  label0 = Widgets.Label("--", 3, 20, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  # initialize PWM on pin with frequency and duty cycle values:
  #pwm1 = PWM(Pin(1), freq=20000, duty=512)
  # initialize PWM on pin 38 (red connector on AtomS3 PortABC):
  pwm1 = PWM(Pin(38))
  # configure PWM duty cycle to 75 to stop the servo:
  pwm1.duty(75)  
  # configure PWM frequency to 50 Hz for the servo:
  pwm1.freq(50)

def loop():
  global pwm1
  M5.update()
  # wait for input and then assign it to input_str variable:
  input_str = input('input servo duty cycle value: ')
  print('received:', input_str)
  # update PWM duty cycle using input value:
  pwm1.duty(int(input_str))
  # display the received input on label0:
  label0.setText(input_str)
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