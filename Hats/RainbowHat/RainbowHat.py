#!/usr/bin/env python

import signal
import rainbowhat
import datetime
import time

timenow = datetime.datetime.now().strftime("%H%M")

def display_message(message):
    rainbowhat.display.print_str(message)
    rainbowhat.display.show()

@rainbowhat.touch.A.press()
def press_a(channel):
#    rainbowhat.rainbow.clear()
    display_message("NOAH") #Display on LED Display
    print ("Button A touched!") #Print to Terminal
    rainbowhat.rainbow.set_all(255,0,0,brightness=0.1) #RGB LEDS - RED
    rainbowhat.rainbow.show()
    rainbowhat.lights.rgb(1,0,0)#Button Light

@rainbowhat.touch.B.press()
def press_b(channel):
#    rainbowhat.rainbow.clear()
    display_message("Jake") 
    print ("Button B touched!") 
    rainbowhat.rainbow.set_all(0,255,0,brightness=0.1)
    rainbowhat.rainbow.show()
    rainbowhat.lights.rgb(0,1,0)

@rainbowhat.touch.C.press()
def press_c(channel):
#    rainbowhat.rainbow.clear()
    display_message("Matt") 
    print ("Button C touched!")
    rainbowhat.rainbow.set_all(0,0,255,brightness=0.1)
    rainbowhat.rainbow.show()
    rainbowhat.lights.rgb(0,0,1)
	
@rainbowhat.touch.release()
def release(channel):
    print("Button release!")
    rainbowhat.rainbow.clear()
    rainbowhat.lights.rgb(0,0,0)
    rainbowhat.buzzer.note(880,0.1)
	
display_message(timenow)
rainbowhat.lights.rgb(1,1,1)
rainbowhat.rainbow.set_pixel(3, 255, 255, 255)
rainbowhat.rainbow.show()
#while True:
#    for pixel in range(7):
#        rainbowhat.rainbow.clear()
#        rainbowhat.rainbow.set_pixel(pixel, 255, 255, 255)
#        rainbowhat.rainbow.show()
#        time.sleep(0.1)


signal.pause()
