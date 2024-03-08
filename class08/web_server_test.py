# beginner program for M5Stack AtomS3 based on uiflow2 code structure

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

import network
import usocket as socket

title0 = None
label0 = None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

ssid = 'ACCD'
password = 'tink1930'

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

print('connect to WiFi...')
while wifi.isconnected() == False:
  print('.', end='')
  time.sleep_ms(100)

print('WiFi connection successful')
print(wifi.ifconfig())

def setup():
  global title0, label0
  M5.begin()
  # display title ("title text", text offset, fg color, bg color, font):
  title0 = Widgets.Title("Web Server", 3, 0x000000, 0xffffff, Widgets.FONTS.DejaVu18)
  # display label ("label text", x, y, layer number, fg color, bg color, font):
  label0 = Widgets.Label("---", 3, 20, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  ip_list = wifi.ifconfig()
  ip_address = ip_list[0]
  label0.setText(ip_address)
  
  
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