# beginner program for M5Stack AtomS3 based on uiflow2 code structure

import os, sys, io
import M5
from M5 import *
from hardware import *
import time
import network
from umqtt import *

title0 = None
label0 = None

ssid = 'INSERT_WIFI_NAME'
password = 'INSERT_WIFI_PASSWORD'

mqtt_client = None
aio_user_name = 'INSERT_YOUR_AIO_USERNAME'
aio_password = 'INSERT_YOUR_AIO_PASSWORD'


def wifi_connect():
  wifi = network.WLAN(network.STA_IF)
  wifi.active(True)
  wifi.connect(ssid, password)

  print('connect to WiFi...')
  while wifi.isconnected() == False:
    print('.', end='')
    time.sleep_ms(100)

  print('WiFi connection successful')
  #print(wifi.ifconfig())
  ip_list = wifi.ifconfig()
  ip_address = ip_list[0]
  print('IP address:', ip_address)

def setup():
  global title0, label0
  global mqtt_client
  M5.begin()
  # display title ("title text", text offset, fg color, bg color, font):
  title0 = Widgets.Title("MQTT test", 3, 0x000000, 0xffffff, Widgets.FONTS.DejaVu18)
  # display label ("label text", x, y, layer number, fg color, bg color, font):
  label0 = Widgets.Label("---", 3, 20, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  wifi_connect()
  mqtt_client = MQTTClient(
      'testclient',
      'io.adafruit.com',
      port = 1883,
      user = aio_user_name,
      password = aio_password,
      keepalive = 0
  )
  mqtt_client.connect(clean_session=True)

  
def loop():
  global mqtt_client
  M5.update()
  if BtnA.wasPressed():
    print('button pressed..')
    mqtt_client.publish(aio_user_name+'/feeds/button-feed', '1', qos=0)
  elif BtnA.wasReleased():
    print('button released..')
    mqtt_client.publish(aio_user_name+'/feeds/button-feed', '0', qos=0)
      
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