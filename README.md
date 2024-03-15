## SP24-IXD-256 Code Repository

Code examples for Adv. Interactive Prototyping class.  

[GitHub Markdown Tutorial](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)  
[Edititing Files on GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)  

### Class 03  

[Digital Input/Output](class03/digital_input_output.py) - turn pin 1 output on/off with AtomS3 screen button input  
[Digital Input/Output Toggle](class03/digital_input_output_toggle.py) - using program state and timer variables to toggle output with button input  
[RGB Output](class03/rgb_output.py) - controlling color RGB LED strips with `fill_color` and `set_color` functions  

### Class 04  

[ADC Test](class04/adc_test.py) - reading Analog to Digital Converter (ADC) input  
[ADC to RGB](class04/adc_to_rgb.py) - mapping analog input to RGB LED output with the custom `map_value` function  
[ADC to RGB Fill and Fade](class04/adc_to_rgb_2states.py) - using analog and button inputs to change between 2 RGB LED behaviors  

### Class 05  

[IMU Test](class05/imu_test.py) - reading Inertial Measurement Unit (IMU) input  
[IMU Tilt and Motion](class05/imu_tilt_and_motion.py) - detecting tilt and motion with IMU acceleration values   
[WebSerial Pyscript Test](class05/webserial_pyscript_test/) - reading Serial input with a graphical software program  
[Print ADC](class05/print_adc.py) - firmware program to test communication with WebSerial PyScript Test example  
[WebSerial PyScript Template](class05/webserial_pyscript_template/) - using Serial input to change  shapes, images, fonts + play sounds  
[Print ADC and Button](class05/print_adc_and_button.py) - firmware program to test communication with WebSerial PyScript Template  
[Print IMU and Button](class05/print_imu_and_button.py) - another program to test communication with WebSerial PyScript Template  

### Class 06  

[Input Example](class06/input_example.py) - simple example of using the `input` function  
[Input to RGB](class06/input_rgb.py) - receiving r,g,b values with `input` to fade RGB LEDs  

### Class 07  

[Servo Module](class07/servo.py) - servo module with `Servo` object class, `move` method, etc.  
[Servo Module Test](class07/servo_module_test.py) - test servo motion with the servo module  
[ADC to Servo](class07/adc_to_servo.py) - control servo motion with analog input  

### Extras  

[AtomS3 Begin](extras/atomS3_begin.py) - beginner template for AtomS3 firwmare  
[RGB Rainbow](extras/rgb_rainbow.py) - rainbow animation or RGB LEDs with the custom `hsb_to_color` function  
