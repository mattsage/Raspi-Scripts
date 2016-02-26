#https://www.raspberrypi.org/learning/quick-reaction-game/
from gpiozero import Button
from picamera import PiCamera

button = Button(17)

with PiCamera() as camera:
    camera.start_preview()
    frame = 1
    while True:
        button.wait_for_press()
        camera.capture('/home/pi/frame%03d.jpg' % frame)
        frame += 1
