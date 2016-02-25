import os
from gpiozero import MotionSensor
import time

pir = MotionSensor(14)

count = 0

while (count < 15):
	if pir.motion_detected:
		os.system("echo `date` >> motiondetected.txt")
		time.sleep(600)
		count = count + 1
	
