import RPi.GPIO as GPIO
import time
import picamera

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT) 

GPIO.output(19, GPIO.HIGH)

with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/evidence.jpg')
    time.sleep(20)
    camera.stop_preview()
    camera.stop_recording('/home/pi/Desktop/evidence.jpg')
    
GPIO.output(19, GPIO.LOW)
