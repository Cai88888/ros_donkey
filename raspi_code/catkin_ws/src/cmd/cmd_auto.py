
## cmd_auto.py

import time
import math
import smbus
import socket
from pynput import keyboard

stop_PWM = 1520
forward_PWM = 1598
start_PWM = forward_PWM + 20

'''
stop_PWM = 1630
start_PWM = stop_PWM + 50
forward_PWM = stop_PWM + 40
'''

class PCA9685:
 
  # Registers/etc.
  __SUBADR1            = 0x02
  __SUBADR2            = 0x03
  __SUBADR3            = 0x04
  __MODE1              = 0x00
  __PRESCALE           = 0xFE
  __LED0_ON_L          = 0x06
  __LED0_ON_H          = 0x07
  __LED0_OFF_L         = 0x08
  __LED0_OFF_H         = 0x09
  __ALLLED_ON_L        = 0xFA
  __ALLLED_ON_H        = 0xFB
  __ALLLED_OFF_L       = 0xFC
  __ALLLED_OFF_H       = 0xFD
 
  def __init__(self, address=0x40, debug=False):
    self.bus = smbus.SMBus(1)
    self.address = address
    self.debug = debug
    if (self.debug):
      print("Reseting PCA9685")
    self.write(self.__MODE1, 0x00)
 
  def write(self, reg, value):
    "Writes an 8-bit value to the specified register/address"
    self.bus.write_byte_data(self.address, reg, value)
    if (self.debug):
      print("I2C: Write 0x%02X to register 0x%02X" % (value, reg))
 
  def read(self, reg):
    "Read an unsigned byte from the I2C device"
    result = self.bus.read_byte_data(self.address, reg)
    if (self.debug):
      print("I2C: Device 0x%02X returned 0x%02X from reg 0x%02X" % (self.address, result & 0xFF, reg))
    return result
 
  def setPWMFreq(self, freq):
    "Sets the PWM frequency"
    prescaleval = 25000000.0    # 25MHz
    prescaleval /= 4096.0       # 12-bit
    prescaleval /= float(freq)
    prescaleval -= 1.0
    if (self.debug):
      print("Setting PWM frequency to %d Hz" % freq)
      print("Estimated pre-scale: %d" % prescaleval)
    prescale = math.floor(prescaleval + 0.5)
    if (self.debug):
      print("Final pre-scale: %d" % prescale)
 
    oldmode = self.read(self.__MODE1);
    newmode = (oldmode & 0x7F) | 0x10        # sleep
    self.write(self.__MODE1, newmode)        # go to sleep
    self.write(self.__PRESCALE, int(math.floor(prescale)))
    self.write(self.__MODE1, oldmode)
    time.sleep(0.005)
    self.write(self.__MODE1, oldmode | 0x80)
 
  def setPWM(self, channel, on, off):
    "Sets a single PWM channel"
    self.write(self.__LED0_ON_L+4*channel, on & 0xFF)
    self.write(self.__LED0_ON_H+4*channel, on >> 8)
    self.write(self.__LED0_OFF_L+4*channel, off & 0xFF)
    self.write(self.__LED0_OFF_H+4*channel, off >> 8)
    if (self.debug):
      print("channel: %d  LED_ON: %d LED_OFF: %d" % (channel,on,off))
 
  def setServoPulse(self, channel, pulse):
    "Sets the Servo Pulse,The PWM frequency must be 50HZ"
    pulse = int(pulse*4096/20000)        #PWM frequency is 50HZ,the period is 20000us
    self.setPWM(channel, 0, pulse)
    
    
pwm = PCA9685(0x40, debug=True)
pwm.setPWMFreq(50)
Stop=0
servo_PWM=1600
def forward():
    global forward_PWM, start_PWM
    pwm.setServoPulse(3,start_PWM)
    time.sleep(0.3)
    pwm.setServoPulse(3,forward_PWM)

def stop():
    global stop_PWM
    pwm.setServoPulse(3,stop_PWM)

def left():
    global servo_PWM
    if(servo_PWM<2100):
        servo_PWM+=50
        pwm.setServoPulse(0,servo_PWM)   
    print(servo_PWM)

def right():
    global servo_PWM
    if(servo_PWM>1200):
        servo_PWM-=50
        pwm.setServoPulse(0,servo_PWM)   
    print(servo_PWM)
    
def on_press(key):
        '按下按键时执行。'
        try:
                if key == keyboard.KeyCode.from_char('enter'):
                        pass
                elif key == keyboard.KeyCode.from_char('w'):
                    print("FORWARD")
                    Stop=0
                    forward()
                elif key == keyboard.KeyCode.from_char('s'):
                    print("STOP")
                    Stop=0
                    stop()
                elif key == keyboard.KeyCode.from_char('a'):
                    print("LEFT")
                    Stop=0
                    left()
                elif key == keyboard.KeyCode.from_char('d'):
                    print("RIGHT")
                    Stop=0
                    right()
                

        except AttributeError:
                print('special key {0} pressed'.format(key))
    #通过属性判断按键类型。

def on_release(key):
    '松开按键时执行。'
    #print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()






# a=0
# pwm.setServoPulse(3,1630)
# time.sleep(0.7)
# pwm.setServoPulse(3,0)
# while True:
#     a=int(input("enter:"))
#     pwm.setServoPulse(0,a)

