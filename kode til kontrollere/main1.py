from machine import Pin, ADC, PWM


from func import *
import time

#Setter alle PWM lave
red.duty(750)
red.freq(500)
green.duty(750)
green.freq(500)
blue.duty(750)
blue.freq(500)


for i in range(24):
        np[i] = (255, 50, 0)
        np.write()
        time.sleep(0.02)
    
for i in range(23, 0, -1):
        np[i] = (0, 0, 0)
        np.write()
        time.sleep(0.02)
    

red.duty(0)
red.freq(500)
green.duty(0)
green.freq(500)
blue.duty(0)
blue.freq(500)

#

while True:
    time.sleep(0.01)
    #print(contrValue.read(), "1")
    if 4000 < contrValue.read() < 4097:
        print("purple")
        purpleOn()
        #print(contrValue.read())
        contrValue.read()
        Off()
    elif 1200 < contrValue.read() < 1300:
        print("blue")
        blueOn()
        #print(contrValue.read())
        contrValue.read()
        Off()
    elif 1550 < contrValue.read() < 1800:
        print("green")
        greenOn()
        #print(contrValue.read())
        contrValue.read()
        Off()
    elif 2600 < contrValue.read() < 2700:
        print("orange")
        orangeOn()
        #print(contrValue.read())
        contrValue.read()
        Off()
    elif 450 < contrValue2.read() < 500:
        print("green2")
        time.sleep(0.4)
        contrValue2.read()
    elif 250 < contrValue2.read() < 300:
        print("blue2")
        time.sleep(0.4)
        contrValue2.read()
    elif 175 < contrValue2.read() < 225:
        print("orange2")
        time.sleep(0.4)
        contrValue2.read()
    elif 1600 < contrValue2.read() < 4095:
        print("purple2")
        time.sleep(0.4)
        contrValue2.read()
        