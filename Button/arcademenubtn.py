from gpiozero import Button
import os

button = Button(17)
button2 = Button(18)

while True:
	if button.is_pressed:
		os.system("ls -l")
		exit()
		
	if button2.is_pressed:
		os.system("startx")
		exit()
