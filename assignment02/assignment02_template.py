# Assignment #2 Template

# read analog input (ADC), button and motion sensor (IMU) values
# display ADC, IMU X and IMU Y values on AtomS3 screen
# print ADC, button values to the Terminal (Serial connection)

# this template can be used with WebSerial Pyscript Template:
# https://pa-nik.github.io/SP24-IXD-256/class05/webserial_pyscript_template/

import os, sys, io
import M5
from M5 import *
from hardware import *
import time
import math

title0 = None
label0 = None
label1 = None
label2 = None
label3 = None

adc1 = None
pin41 = None

update_timer = 0
motion_timer = 0
program_state = 'IDLE'

imu_x_val = 0.0   # X-axis acceleration value
imu_y_val = 0.0   # Y-axis acceleration value
imu_y_last = 0.0  # last Y-axis acceleration value

def setup():
  global title0, label0, label1, label2, label3, adc1, pin41
  M5.begin()
  
  # initialize title ("title text", text offset, fg color, bg color, font):
  title0 = Widgets.Title("assignment2", 3, 0x000000, 0xffffff, Widgets.FONTS.DejaVu18)
  
  # initialize labels ("label text", x, y, layer number, fg color, bg color, font): 
  label0 = Widgets.Label("--", 3, 30, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  label1 = Widgets.Label("--", 3, 50, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  label2 = Widgets.Label("--", 3, 70, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  label3 = Widgets.Label("--", 4, 90, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  
  # initialize analog to digital converter on pin 1:
  adc1 = ADC(Pin(1), atten=ADC.ATTN_11DB)
  
  # initialize pin 41 (screen button on AtomS3 board) as input:
  pin41 = Pin(41, mode=Pin.IN)

# function to map input value range to output value range:
def map_value(in_val, in_min, in_max, out_min, out_max):
  out_val = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
  if out_val < out_min:
    out_val = out_min
  elif out_val > out_max:
    out_val = out_max
  return int(out_val)

# function to get single RGB color value from r, g, b values:
def get_color(r, g, b):
  rgb_color = (r << 16) | (g << 8) | b
  return rgb_color

def loop():
  global label0, label1, label2, label3, adc1
  global update_timer, motion_timer, program_state
  global adc1_val, imu_x_val, imu_y_val, imu_y_last
  
  M5.update()
  
  # read ADC value:
  adc1_val = adc1.read()
  
  # read button value:
  button_value = pin41.value()
  
  # map the ADC value from 0-4095 to 0-255 range:
  adc1_val_8bit = map_value(adc1_val, 0, 4095, 0, 255)
  
  # read the IMU accelerometer values:
  imu_val = Imu.getAccel()
  
  imu_x_val = imu_val[0]  # update X-axis acceleration value
  # map IMU X-axis acceleration from -1.0 - 1.0 to 0 - 255 range:
  imu_x_val_8bit = map_value(imu_y_val, -1.0, 1.0, 0, 255)
  
  imu_y_last = imu_y_val  # save the last imu_y_val
  imu_y_val = imu_val[1]  # update Y-axis acceleration value
  # map IMU Y-axis acceleration from 0.0 - 1.0 to 0 - 255 range:
  imu_y_val_8bit = map_value(imu_y_val, 0.0, 1.0, 0, 255)

  # Y-axis acceleration difference (absolute value):
  imu_y_diff = imu_y_val - imu_y_last
  
  if program_state == 'IDLE':
    # change from IDLE to MOTION state when motion is detected:
    if imu_y_diff > 0.25 or imu_y_diff < -0.25:
      program_state = 'MOTION'
      # reset motion timer:
      motion_timer = time.ticks_ms()
  elif program_state == 'MOTION':
    # change back to IDLE state 3 seconds after motion was detected:
    if(time.ticks_ms() > motion_timer + 3000):
      program_state = 'IDLE'

  # update every 100 ms (10 times per second):
  if time.ticks_ms() > update_timer + 100:
    # update update_timer with current time in milliseconds:
    update_timer = time.ticks_ms()
    
    red = get_color(adc1_val_8bit, 0, 0)
    green = get_color(0, imu_x_val_8bit, 0)
    blue = get_color(0, 0, imu_y_val_8bit)
  
    # show ADC value on label0:
    label0.setText('ADC: ' + str(adc1_val))
    # set foreground color to white, background color to red value:
    label0.setColor(0xffffff, red)
    
    # show IMU X-axis acceleration with 0.2 precision on display label1:
    imu_x_str = 'IMU X: {:0.2f}'.format(imu_x_val)
    label1.setText(imu_x_str)
    # set foreground color to white, background color to green value:
    label1.setColor(0xffffff, green)
    
    # show IMU X-axis acceleration with 0.2 precision on display label2:
    imu_y_str = 'IMU Y: {:0.2f}'.format(imu_y_val)
    label2.setText(imu_y_str)
    # set foreground color to white, background color to blue value:
    label2.setColor(0xffffff, blue)
    
    # show program_state on display label:
    label3.setText(program_state)
    
    # print the 8-bit ADC value ending with comma:
    print(adc1_val_8bit, end=',')
    # print the button value:
    print(button_value)
    

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