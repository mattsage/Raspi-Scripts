#To make your own Crackerjoke-a-tron, you’ll need:

#1 x Raspberry Pi (any model will work)
#2 x tactile push buttons
#1 x speaker with a standard 2.5 mm jack
#1 x breadboard
#2 x male-to-male jumper leads
#5 x female-to-male jumper leads
#1 x red LED
#1 x green LED
#2 x 330 ohm resistors

#Create a new folder on your Pi called ‘crackerjoke’ by entering the following into a terminal window:

mkdir crackerjoke

cd crackerjoke

#To download the .wav files to your Pi, use this:

wget http://rpf.io/goodjoke -O goodjoke.wav
wget http://rpf.io/badjoke -O badjoke.wav

#To make sure the files play, try typing the following (make sure to plug in your speaker or some headphones):

aplay goodjoke.wav

#The GPIO pins we are using are as follows:

#Good joke button = pin 21
#Bad joke button = pin 24
#Red LED = pin 8
#Green LED = pin 7

#Now it’s time for the code. Open Python 3, create a new file within the crackerjoke folder called ‘crackerjoke.py’ and type the following:
#################################################################
import pygame.mixer
from pygame.mixer import Sound
from gpiozero import Button, LED
from signal import pause
from time import sleep

pygame.mixer.init()

good = Sound("/home/pi/crackerjoke/goodjoke.wav")
bad = Sound("/home/pi/crackerjoke/badjoke.wav")

goodbutton = Button(21)
badbutton = Button(24)

red = LED(8)
green = LED(7)

while True:
   red.on()
   green.on()
   goodbutton.when_pressed = good.play
   badbutton.when_pressed = bad.play

pause()
#################################################################

#If you’d like the code to run on reboot, allowing you to detach yourself from the monitor, keyboard, and mouse, open a terminal window and type:
nano ~/.config/lxsession/LXDE-pi/autostart
#At the bottom of the file, add:
@python /home/pi/crackerjoke/crackerjoke.py
#Save and reboot.
