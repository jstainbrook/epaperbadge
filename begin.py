#!/usr/bin/env python

import signal
import buttonshim
import subprocess
import time

print("""

Button A - My Name is Julie Stainbrook
Button B - My Name is hyperjoule.io
Button C - hyperjoule.io qr code
Button D - Month Calendar
Button E - Clean Screen
Press Ctrl+C to exit.

""")
## globals -- set these for button a and b
name = "Your Name"
website = "Your Website"
###########################################


buttonshim.set_pixel(0x00,0x00,0x00)
buttonshim.set_pixel(0x80,0xff,0xdd)
time.sleep(1)
buttonshim.set_pixel(0x00,0x00,0x00)
@buttonshim.on_press(buttonshim.BUTTON_A)

def button_a(button, pressed):
    global name
    buttonshim.set_pixel(0x94, 0x00, 0xd3)
    subprocess.Popen('sudo /home/pi/scripts/hello.py '+name+' red', shell=True)

@buttonshim.on_press(buttonshim.BUTTON_B)
def button_b(button, pressed):
    global website
    buttonshim.set_pixel(0x00, 0x00, 0xff)
    subprocess.Popen('sudo /home/pi/scripts/hello.py '+website+' red', shell=True)

@buttonshim.on_press(buttonshim.BUTTON_C)
def button_c(button, pressed):
    buttonshim.set_pixel(0x00, 0xff, 0x00)
    subprocess.Popen('sudo /home/pi/scripts/qr.py red "http://www.yourwebsite.com"', shell=True)

@buttonshim.on_press(buttonshim.BUTTON_D)
def button_d(button, pressed):
    buttonshim.set_pixel(0xff, 0xff, 0x00)
    subprocess.Popen('sudo /home/pi/scripts/cal.py red', shell=True)

@buttonshim.on_press(buttonshim.BUTTON_E)
def button_e(button, pressed):
    buttonshim.set_pixel(0xff, 0x00, 0x00)
    subprocess.Popen('sudo /home/pi/scripts/clean.py red 1', shell=True)

signal.pause()
