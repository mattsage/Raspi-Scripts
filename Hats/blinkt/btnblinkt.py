#!/usr/bin/env python

import signal
import buttonshim
import blinkt
import os

blinkt.set_clear_on_exit()

@buttonshim.on_press(buttonshim.BUTTON_A)
def button_a(button, pressed):
    buttonshim.set_pixel(128, 0, 0)
	blinkt.set_all(128, 0, 0)

@buttonshim.on_press(buttonshim.BUTTON_B)
def button_b(button, pressed):
    buttonshim.set_pixel(0, 128, 0)
	blinkt.set_all(0, 128, 0)

@buttonshim.on_press(buttonshim.BUTTON_C)
def button_c(button, pressed):
	buttonshim.set_pixel(0, 0, 128)
	blinkt.set_all(0, 0, 128)

@buttonshim.on_press(buttonshim.BUTTON_D)
def button_d(button, pressed):
    buttonshim.set_pixel(0xff, 0xff, 0x00)

@buttonshim.on_press(buttonshim.BUTTON_E)
def button_e(button, pressed):
    buttonshim.set_pixel(0xff, 0x00, 0x00)

@buttonshim.on_hold(buttonshim.BUTTON_E, hold_time=2)
def button_e(button, pressed):
    buttonshim.set_pixel(0xff, 0x00, 0x00)
	os.system("sudo poweroff")
	
signal.pause()
