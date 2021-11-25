from machine import Pin, ADC, PWM
import neopixel
import time

import machine
import neopixel
import time


n = 24

p = 25

np = neopixel.NeoPixel(Pin(p), n)

for i in range(24):
    np[i] = (255, 50, 0)
    np.write()
    time.sleep(0.02)
    
for i in range(23, 0, -1):
    np[i] = (0, 0, 0)
    np.write()
    time.sleep(0.02)
    
    


#kontroller nr. 1
p15 = Pin(15, Pin.OUT)
red = PWM(p15)
p4 = Pin(4, Pin.OUT)
green = PWM(p4)
p5 = Pin(5, Pin.OUT)
blue = PWM(p5)
p12 = Pin(12, Pin.OUT)
p14 = Pin(14, Pin.OUT)
p27 = Pin(27, Pin.OUT)
p26 = Pin(26, Pin.OUT)
contrValue = ADC(Pin(34))
contrValue.atten(ADC.ATTN_11DB)


def purpleOn():
    red.duty(750)
    red.freq(500)
    green.duty(0)
    green.freq(500)
    blue.duty(750)
    blue.freq(500)
    
    for i in range(24):
        np[i] = (255, 0, 255)
        np.write()
        time.sleep(0.01)
    
    for i in range(23, 0, -1):
        np[i] = (0, 0, 0)
        np.write()
        time.sleep(0.01)
    p12.value(1)
    time.sleep(0.3)
    p12.value(0)
        
def orangeOn():
    red.duty(750)
    red.freq(500)
    green.duty(150)
    green.freq(500)
    blue.duty(0)
    blue.freq(500)
     
    for i in range(24):
        np[i] = (255, 50, 0)
        np.write()
        time.sleep(0.01)
    
    for i in range(23, 0, -1):
        np[i] = (0, 0, 0)
        np.write()
        time.sleep(0.01)
    p14.value(1)
    time.sleep(0.3)
    p14.value(0)
        
def blueOn():
    red.duty(0)
    red.freq(500)
    green.duty(0)
    green.freq(500)
    blue.duty(750)
    blue.freq(500)
    
    for i in range(24):
        np[i] = (0, 0, 255)
        np.write()
        time.sleep(0.01)
    
    for i in range(23, 0, -1):
        np[i] = (0, 0, 0)
        np.write()
        time.sleep(0.01)
    p27.value(1)
    time.sleep(0.3)
    p27.value(0)
        
def greenOn():
    red.duty(0)
    red.freq(500)
    green.duty(750)
    green.freq(500)
    blue.duty(0)
    blue.freq(500)
    
    for i in range(24):
        np[i] = (0, 255, 0)
        np.write()
        time.sleep(0.01)
    
    for i in range(23, 0, -1):
        np[i] = (0, 0, 0)
        np.write()
        time.sleep(0.01)
    p26.value(1)
    time.sleep(0.3)
    p26.value(0)
def Off():
    red.duty(0)
    green.duty(0)
    blue.duty(0)



