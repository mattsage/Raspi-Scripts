import RPi.GPIO as GPIO

import time
import picamera

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT) 

GPIO.output(19, GPIO.HIGH)

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(5)
    camera.capture('/home/pi/Desktop/test.jpg')
    camera.stop_preview()

GPIO.output(19, GPIO.LOW)    
