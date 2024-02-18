### WebSerial Test  
  
The files in this directory show a simple example of reading input from hardware with a software program written in Python syntax, by combining [PyScript](https://pyscript.net/) with the [p5 Graphics Library](https://p5js.org/) using [Web Serial API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Serial_API).  

The software program can be previewed running and responding to input online by following these steps:

1. use Thonny to run a firmware example such as [print_adc.py](../print_adc.py) on your AtomS3 hardware with one analog input connected, such as the M5Stack ANGLE unit.  Observe that values in the range 0 - 255 are printed to the terminal in Thonny.  

2. disconnect from AtomS3 (change the Python interpreter to "Local Python 3" option at the bottom right of Thonny window).  The firmware program should still be running and updating the display on AtomS3.

3. go to the [GitHub Pages link for this directory](https://pa-nik.github.io/SP24-IXD-256/class05/webserial_pyscript_test/) and click the 'Connect' button.  You should see the number value under the button updated and a circle shape change its size in response to the value.

![screencap_webserial_test.png](screencap_webserial_test.png)