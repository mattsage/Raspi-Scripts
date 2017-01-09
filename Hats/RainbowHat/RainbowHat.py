#!/usr/bin/env python

import signal
import rainbowhat
import os

def display_message(message):
    rainbowhat.display.print_str(message)
    rainbowhat.display.show()

@rainbowhat.touch.A.press()
def press_a(channel):
    display_message("AHOY")
	print ("Button A touched!")
    rainbowhat.lights.rgb(1,0,0)

@rainbowhat.touch.B.press()
def press_b(channel):
    display_message("YARR")
	print ("Button A touched!")
    rainbowhat.lights.rgb(0,1,0)

@rainbowhat.touch.C.press()
def press_c(channel):
    display_message("GROG")
	print ("Button A touched!")
    rainbowhat.lights.rgb(0,0,1)

	
display_message("ABC.")
rainbowhat.lights.rgb(1,1,1)
