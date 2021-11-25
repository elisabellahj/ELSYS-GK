import time
import serial
import os
from pynput.keyboard import Controller
import pyautogui

serialPort = serial.Serial(port = "COM3", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

serialString = ""

keyboard = Controller()

time.sleep(1)


os.system("start C:\\Users\\andre\\Desktop\\quiz_app_final.py") 
time.sleep(1)
pyautogui.press("tab")

while True:

    if(serialPort.in_waiting > 0):  

        serialString = ((serialPort.readline()).decode("UTF-8")).strip()

        print(serialString)

        
        time.sleep(1)
        
        if serialString == "orange":
            keyboard.type("1")
        elif serialString == "purple":
            keyboard.type("2")
        elif serialString == "blue":
            keyboard.type("3")
        elif serialString == "green":
            keyboard.type("4")
        elif serialString == "orange2":
            keyboard.type("5")
        elif serialString == "purple2":
            keyboard.type("6")
        elif serialString == "blue2":
            keyboard.type("7")
        elif serialString == "green2":
            keyboard.type("8")
        else:
        
            print(serialString, type(serialString))
            print("funker ikke")
